import re

class WAFMiddleware:
    def __init__(self):
        self.rules = [
            (re.compile(r"(?i)<script|onerror|onload"), "XSS Attempt"),
            (re.compile(r"(?i)union\s+select"), "SQLi Attempt"),
            (re.compile(r"(?i)\.\./\.\./"), "Path Traversal")
        ]
    def inspect_payload(self, request_data):
        for pattern, rule_name in self.rules:
            if pattern.search(request_data):
                print(f"[WAF BLOCK] Dropped request. Triggered Rule: {rule_name}")
                return False
        print("[WAF ALLOW] Payload is clean.")
        return True

waf = WAFMiddleware()
test_payloads = [
    "GET /home HTTP/1.1",
    "GET /page?q=<script>alert('test')</script> HTTP/1.1",
    "GET /search?q=UNION SELECT name FROM test HTTP/1.1",
    "GET /image?file=../../etc/passwd HTTP/1.1" ]

for payload in test_payloads:
    print(f"\nTesting: {payload}")
    waf.inspect_payload(payload)