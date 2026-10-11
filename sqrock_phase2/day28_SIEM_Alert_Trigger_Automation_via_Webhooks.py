import requests
import json

def send_alert_webhook(webhook_url, alert_data):
    headers = {"Content-Type": "application/json"}
    payload = {"text": (f"**CRITICAL SECURITY ALERT**\n**Type:** {alert_data['type']}\n**Source:** {alert_data['ip']}")}
    print(f"[*] Dispatching webhook to {webhook_url[:20]}...")

    # Simulated execution
    # response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    print("[+] Webhook dispatched successfully.")

    print("\nPayload:")
    print(json.dumps(payload, indent=4))

send_alert_webhook( "https://hooks.slack.com/services/T000/B000/XXX",
    {"type": "Multiple Failed Logins", "ip": "10.0.0.5"} )