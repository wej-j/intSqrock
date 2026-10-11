from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Local Day 20 test server"

@app.route("/admin")
def admin():
    return "Admin test page"

@app.route("/dashboard")
def dashboard():
    return "Dashboard test page"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)