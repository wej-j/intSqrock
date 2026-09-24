import whois
import socket
import requests


def osint_scan(domain):
    w = whois.whois(domain)
    ip = socket.gethostbyname(domain)
    geo = requests.get(
        f"http://ip-api.com/json/{ip}",
        timeout=10
    ).json()

    print("\n=== OSINT RESULTS ===")
    print(f"Registrar: {w.registrar}")
    print(f"IP: {ip}")

    if geo.get("status") == "success":
        print(
            f"Location: {geo.get('city')}, "
            f"{geo.get('country')}"
        )
    else:
        print("Location lookup unavailable.")