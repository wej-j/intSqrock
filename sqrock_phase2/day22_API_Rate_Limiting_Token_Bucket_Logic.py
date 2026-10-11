import time

class RateLimiter:
    def __init__(self, token_capacity, refill_rate_per_second):
        self.capacity = token_capacity
        self.refill_rate = refill_rate_per_second
        self.ledger = {}
    def allow_request(self, client_ip):
        now = time.time()
        if client_ip not in self.ledger:
            self.ledger[client_ip] = {"tokens": self.capacity, "last_updated": now}
        state = self.ledger[client_ip]
        elapsed = now - state["last_updated"]
        state["tokens"] = min(self.capacity, 
                              state["tokens"] + (elapsed * self.refill_rate))
        state["last_updated"] = now
        if state ["tokens"] >= 1:
            state["tokens"] -= 1
            return True
        return False

# Local orchestration check simulating rapid requests
limiter = RateLimiter(token_capacity=3, refill_rate_per_second=0.5)

client_ip = "127.0.0.1"
print("[*] Simulating rapid API requests...\n")
for request_number in range(1, 7):
    allowed = limiter.allow_request(client_ip)

    if allowed:
        print(f"[+] Request {request_number}: ALLOWED")
    else:
        print(f"[-] Request {request_number}: DENIED - Rate limit reached")
print("\n[*] Waiting 2 seconds for token refill...")
time.sleep(2)

if limiter.allow_request(client_ip):
    print("[+] Request after refill: ALLOWED")
else:
    print("[-] Request after refill: DENIED")