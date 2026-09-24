def fake_profile_score(profile):
    score = 0
    age_days = profile.get("account_age_days", 365)
    if age_days < 30:  score += 30
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)
    ratio = following / max(followers, 1)
    if ratio > 10:  score += 25
    if profile.get("no_profile_pic"):  score += 20
    if profile.get("posts", 100) < 5:  score += 15
    if profile.get("default_bio"):  score += 10
    return min(score, 100)

profiles = [
    #Prof_1
    {"account_age_days":7, "followers":2, "following":900,
     "no_profile_pic":True, "posts":1, "default_bio":True},
    #Prof_2
    {"account_age_days":1200, "followers":4500, "following":320,
     "no_profile_pic":False, "posts":1, "default_bio":False},
    #Prof_3
    {"account_age_days":18, "followers":12, "following": 420,
     "no_profile_pic":True, "posts":3, "default_bio":True},
    #Prof_4
    {"account_age_days":850, "followers":300, "following":250,
     "no_profile_pic":False, "posts":95, "default_bio":False},
    #Prof_5
    {"account_age_days":45, "followers":20, "following":400,
     "no_profile_pic":False, "posts":10, "default_bio":True},
    #prof_6
    {"account_age_days":10, "followers":150, "following":100,
     "no_profile_pic":True, "posts":2, "default_bio":False},
    #Prof_7
    {"account_age_days":1200, "followers":2500, "following":600,
     "no_profile_pic":False, "posts":400, "default_bio":False},
]

for i, p in enumerate(profiles):
    print(f"Profile {i+1} -> Fake Score: {fake_profile_score(p)}%")
