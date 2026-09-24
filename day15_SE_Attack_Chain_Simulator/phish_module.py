import re
from urllib.parse import urlparse


KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal"
]


def phish_score(url):
    parsed = urlparse(url)
    score = 0

    if not url.startswith("https"):
        score += 30

    for keyword in KEYWORDS:
        if keyword in parsed.netloc.lower():
            score += 20

    if parsed.netloc.count(".") > 3:
        score += 25

    if re.search(
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
        parsed.netloc
    ):
        score += 40

    return min(score, 100)