import datetime
import json
import os


def ir_response(incident):
    print("\n=== INCIDENT RESPONSE TRIGGERED ===")
    print(f"Time: {datetime.datetime.now()}")
    print(f"Type: {incident['type']}")
    print(f"Severity: {incident['severity']}")
    print(f"User: {incident['user']}")

    actions = []

    if incident["severity"] in ("HIGH", "CRITICAL"):
        actions += [
            "LOCK user account",
            "Revoke active sessions",
            "Notify SOC team",
            "Preserve mail logs"
        ]

    if incident["type"] == "phishing":
        actions += [
            "Quarantine email",
            "Block sender domain",
            "Scan attachments in sandbox"
        ]

    print("\nSimulated Actions:")

    if actions:
        for action in actions:
            print(f"[x] {action}")
    else:
        print("[i] No predefined automated actions for this incident.")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    folder = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(folder, "ir_report.json")

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print("\nIR report saved: ir_report.json")