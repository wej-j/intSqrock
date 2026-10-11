import re

MOCK_ACCESS_LOGS = [
    '192.168.1.45 - "GET /profile?id=5 HTTP/1.1" 200',
    '10.0.4.12 - "POST /auth/login?user=admin%27%20OR%20%271%27=%271 HTTP/1.1" 401',
    '172.16.5.9 - "GET /search?q=UNION%20SELECT%20null,password%20FROM%20users-- HTTP/1.1" 500'
]

def analyze_sqli_signatures(logs):
    sqli_regex = re.compile(
        r"(?i)('|--|#|UNION(?:%20|\s)+SELECT|OR(?:%20|\s)+\d+=\d+)"
    )

    for entry in logs:
        # Decode URL-encoded characters to make the log entry more readable
        decoded_entry = entry.replace("%20", " ").replace("%27", "'")

        if sqli_regex.search(decoded_entry):
            source_ip = entry.split(" ")[0]
            print(f"[CRITICAL MALICIOUS PATTERN] Source: {source_ip} -> String: {entry}")

analyze_sqli_signatures(MOCK_ACCESS_LOGS)