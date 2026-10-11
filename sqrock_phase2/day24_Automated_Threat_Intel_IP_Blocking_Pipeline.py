import json

MOCK_INTEL_FEED = [
    {"ip": "103.45.67.89", "indicator": "malware_c2", "risk_score": 98},
    {"ip": "185.10.11.12", "indicator": "botnet_node", "risk_score": 85},
    {"ip": "198.51.100.33", "indicator": "brute_forcer", "risk_score": 92}]

def update_firewall_rules(feed_data):
    print("[*] Ingesting Threat Intelligence Feed...")
    results = []
    for entry in feed_data:
        if entry.get("risk_score", 0) > 90:
            action = "BLOCK"
            print(
                f"[ACTION] HIGH RISK - Deploying block rule for IP: "
                f"{entry['ip']} (Reason: {entry['indicator']})")
        else:
            action = "MONITOR"
            print(
                f"[*] LOGGING - Suspicious activity monitored for IP: "
                f"{entry['ip']}")
        results.append({
            "ip": entry["ip"],
            "indicator": entry["indicator"],
            "risk_score": entry["risk_score"],
            "action": action
        })
    with open("day24_results.json", "w") as file:
        json.dump(results, file, indent=4)
    print("\n[+] Results saved: day24_results.json")

update_firewall_rules(MOCK_INTEL_FEED)