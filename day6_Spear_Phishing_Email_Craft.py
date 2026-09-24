def spear_phish_template(target):
    return f"""
From : it-support@{target['company'].lower()}.com
To : {target['email']}
Subject : Action Required: Your {target['company']} account will be disabled

Hi {target['name']},

Our security team noticed a login from {target['location']}.
Please verify your account within 24 hours to avoid suspesion.

[Verify Account] -> https://lab.internal/awareness-test

Regards,
IT Security Team
"""

targets =[
    {
    "name": "Riya Sharma",
    "email": "riya@company.com",
    "company": "Sqrock",
    "location": "Bangalore, India"
    },
    {
        "name": "Alex Morgan",
        "email": "alex@example.com",
        "company": "ExampleCorp",
        "location": "Rome, Italy"
    },
    {
        "name": "Sam Taylor",
        "email": "sam@example.org",
        "company": "DemoTech",
        "location": "New York, USA"
    },
    {
        "name": "Jordan Lee",
        "email": "jordan@example.net",
        "company": "TrainingLab",
        "location": "Paris, France"
    }]

for target in targets:
    print(spear_phish_template(target))