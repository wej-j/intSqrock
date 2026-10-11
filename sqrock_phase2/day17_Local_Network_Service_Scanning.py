import socket

def scan_local_port(host, ports):
    print(f"[*] Initiating Socket Sweep on: {host}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        state = sock.connect_ex((host, port))
        if state == 0:
            print(f"[!] OPEN SERVICE DETECTED: Port {port}")
        sock.close()

scan_local_port("127.0.0.1", [22, 80, 443, 5432, 8080])