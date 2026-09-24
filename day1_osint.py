import whois, socket, requests

def osint_scan(domain):
    w = whois.whois(domain)
    ip = socket.gethostbyname(domain)
    geo = requests.get(f"http://ip-api.com/json/{ip}").json()
    print(f"Registrar: {w.registrar}")
    print(f"IP: {ip}")
    print(f"Location: {geo['city']}, {geo['country']}")

osint_scan("example.com")