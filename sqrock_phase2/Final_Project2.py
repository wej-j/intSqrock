import socket, requests, re, html, json
from urllib.parse import urlparse

class AutomatedScanner:
    def __init__(self, target):
        # Store the target URL and extract its hostname for socket scanning
        self.target = target.rstrip("/")
        self.host = urlparse(target).hostname
        # Store all findings discovered during the scan
        self.findings = []

    def run_recon(self):
        # Perform basic reconnaissance by checking selected ports
        # and testing common web application paths
        print(f"\n[*] Running Reconnaissance on {self.target}...")

        # Scan a predefined list of commonly used service ports
        ports = [22, 80, 443, 5432, 5000, 8080]

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            state = sock.connect_ex((self.host, port))
            if state == 0:
                print(f"[+] Open port detected: {port}")
                self.findings.append({
                    "module": "Port Scan",
                    "finding": f"Open port {port}" })
            sock.close()

        # Test common application routes for accessible or restricted resources
        paths = [
            "admin", "dashboard", "api/v1", ".env", "backup.sql" ]

        for path in paths:
            url = f"{self.target}/{path}"
            try:
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    print(f"[+] Accessible route: {url}")
                    self.findings.append({
                        "module": "Directory Discovery",
                        "finding": f"Accessible route: /{path}" })
                elif response.status_code == 403:
                    print(f"[!] Restricted route detected: {url}")
                    self.findings.append({
                        "module": "Directory Discovery",
                        "finding": f"Restricted route: /{path}" })
            except requests.RequestException:
                pass

    def run_vuln_checks(self):
        # Run simple vulnerability checks against mock log data
        # and demonstrate XSS input sanitization
        print("\n[*] Executing Vulnerability Audits...")

        # Simulated web access logs containing normal and suspicious requests
        mock_logs = [
            '192.168.1.45 - "GET /profile?id=5 HTTP/1.1" 200',
            '10.0.4.12 - "POST /auth/login?user=admin%27%20OR%20%271%27=%271 HTTP/1.1" 401',
            '172.16.5.9 - "GET /search?q=UNION%20SELECT%20null,password%20FROM%20users-- HTTP/1.1" 500' ]

        # Search the logs for common SQL injection indicators
        sqli_regex = re.compile(r"(?i)('|--|#|UNION\s+SELECT|OR\s+\d+=\d+)")

        for entry in mock_logs:
            # Decode selected URL-encoded characters before inspection
            decoded = entry.replace("%20", " ").replace("%27", "'")
            if sqli_regex.search(decoded):
                source_ip = entry.split(" ")[0]
                print(f"[!] SQLi pattern detected from: {source_ip}")
                self.findings.append({ "module": "SQLi Detection",
                    "finding": f"Suspicious SQLi pattern from {source_ip}" })

        # Demonstrate neutralization of potentially unsafe XSS input
        xss_input = "<script>alert('XSS')</script>"
        encoded = html.escape(xss_input)
        sanitized = re.sub(r"(?i)script|onerror|onload", "[PROHIBITED_TOKEN]", encoded )
        print(f"[+] XSS input sanitized: {sanitized}")

    def generate_report(self):
        # Create a structured JSON report containing all collected findings
        print("\n[*] Compiling Final Security Report...")

        report = {
            "target": self.target,
            "total_findings": len(self.findings),
            "findings": self.findings}

        # Save the final scan results to a JSON file
        with open("day30_scan_report.json", "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)
            print(f"[+] Total findings: {len(self.findings)}")

        print("[+] Report saved: day30_scan_report.json")

if __name__ == "__main__":
    # Start the complete local vulnerability scanning workflow
    print("=== PHASE 2 FINAL PROJECT ===")
    scanner = AutomatedScanner("http://127.0.0.1:5000")
    scanner.run_recon()
    scanner.run_vuln_checks()
    scanner.generate_report()

    print("\n[-] Scan Complete.")