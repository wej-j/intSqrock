def awareness_email_template(target):
    return f"""
=== PHISHING AWARENESS TRAINING EMAIL ===

From: training-it@example.com
To: {target['email']}
Subject: Action Required: Account Verification

Hi {target['name']},

This is a simulated awareness-training message.

A fictional security notification claims that unusual
activity was detected near {target['location']}.

[Training Link]
https://example.com/awareness-test

RED FLAGS:
- Unexpected urgency
- Account warning
- Request to follow a link
- Personalized information

This email is for awareness training only.
"""