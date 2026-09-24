from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime, json

LOG = []
class HoneyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        entry = {
            "time" : str(datetime.datetime.now()),
            "ip"   : self.client_address[0],
            "path" : self.path,
            "agent": self.headers.get("User-agent", "?") }
        LOG.append(entry)
        print(json.dumps(entry))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Thanks for visiting!")

    def log_message(self, *args): pass #suppress default logs

print("Honeypot on http://127.0.0.1:8080")
HTTPServer(("127.0.0.1", 8080), HoneyHandler).serve_forever()