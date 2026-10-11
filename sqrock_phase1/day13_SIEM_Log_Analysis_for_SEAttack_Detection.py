import re
from collections import Counter

LOG_SAMPLE = """
2024-01-15 02:34:12 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:14 FAILED_LOGIN user=admin ip=45.33.32.156
2024-01-15 02:34:16 SUCCESS_LOGIN user=admin ip=45.33.32.156
2024-01-15 08:00:01 SUCCESS_LOGIN user=riya ip=192.168.1.10
2024-01-15 02:35:00 EMAIL_RULE_CREATED user=admin rule=forward_all
"""

def analyze_logs(logs):
    fails = re.findall(
        r'FAILED_LOGIN user=(\w+) ip=([\d.]+)',
        logs
    )
    rules = re.findall(
        r'EMAIL_RULE_CREATED user=(\w+)',
        logs
    )
    fail_counts = Counter(u for u, _ in fails)

    for user, count in fail_counts.items():
        if count >= 3:
            print(
                f"[ALERT] Brute Force detected: {user} ({count} failures)"
            )

    for user in rules:
        print(f"[ALERT] Suspicious email rule created by: {user}")

analyze_logs(LOG_SAMPLE)