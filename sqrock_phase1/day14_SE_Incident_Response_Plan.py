import datetime, json

def ir_response(incident):
    print(f"\n=== INCIDENT RESPONSE TRIGGERED ===")
    print(f"Time    : {datetime.datetime.now()}")
    print(f"Type    : {incident['type']}")
    print(f"Severity: {incident['severity']}")
    actions = []
    if incident['severity'] in ('HIGH', 'CRITICAL'):
        actions += ["LOCK user account", "Revoke active sessions",
                    "Notify SOC team", "Preserve mail logs"]
    if incident['type'] == 'phishing':
        actions += ["Quarantine email", "Block sender domain", 
                    "Scan attachments in sandbox"]
    print("\nActions Taken:")
    for a in actions:
        print(f" [x] {a}")
    report = {"incident": incident, "actions": actions,
              "timestamp": str(datetime.datetime.now())}
    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nIR report saved: ir_report.json")
ir_response({"type":"phishing", "severity": "HIGH", "user":"riyasqrock.com"})