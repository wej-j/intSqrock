import requests
import json


def github_profile(username):
    base = "https://api.github.com"

    user = requests.get(
        f"{base}/users/{username}",
        timeout=10
    ).json()

    repos = requests.get(
        f"{base}/users/{username}/repos",
        timeout=10
    ).json()

    langs = {}

    for repo in repos[:10]:
        if repo.get("language"):
            language = repo["language"]
            langs[language] = langs.get(language, 0) + 1

    profile = {
        "name": user.get("name"),
        "company": user.get("company"),
        "location": user.get("location"),
        "public_repos": user.get("public_repos"),
        "top_langs": langs,
        "bio": user.get("bio")
    }

    print("\n=== PUBLIC GITHUB PROFILE ===")
    print(json.dumps(profile, indent=2))

    return profile