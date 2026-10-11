import requests, re

def harvest_emails(url):
    html = requests.get(url, timeout=10).text
    emails = set(re.findall(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}', html))
    return emails

found = harvest_emails("http://localhost:8000/practice.html")
for e in found:
    print (e)