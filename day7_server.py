from flask import Flask, request

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "letmein"

failed_attempts = 0
MAX_ATTEMPTS = 3

@app.route("/login", methods=["POST"])
def login():
    global failed_attempts

    username = request.form.get("username")
    password = request.form.get("password")

    # Rate limit check
    if failed_attempts >= MAX_ATTEMPTS:
        return "Too many failed attempts. Try again later.", 429

    if username == USERNAME and password == PASSWORD:
        failed_attempts = 0  # Reset failed attempts on successful login
        return "Welcome", 200

    # Wrong login
    failed_attempts += 1
    return f"Invalid credentials. Failed attempts: {failed_attempts}", 401

if __name__ == "__main__":
    app.run(port=5000)