def generate_vishing_script(target_company, attacker_role, pretext, opener, hook):
    script = f"""
=== VISHING AWARNESS SCRIPT ===
Caller Role: {attacker_role}
Target Org: {target_company}
Pretext: {pretext}

[OPENER]
'{opener}'

[HOOK]
'{hook}'

[RED FLAG for Awarness]
->Legitimate IT will NEVER ask for passwords.
->Always verify via official internal channels.
"""
    return script

print(generate_vishing_script("Sqrock IT", "IT Support", "Password Reset", "Hi, this is Alex from IT Support at Sqrock IT.", 
                              "I need to verify your identity - can you confirm your employee ID and current password?"))

# 3 unique scripts

# 1. IT Support Scenario
print(generate_vishing_script("Example Company", "IT Support", "Password Reset",
    "Hello, this is Alex from IT Support. We detected a problem with your account.",
    "To continue, I need you to confirm your current password and login credentials. Please provide them now."
))

# 2. Bank Scenario
print(generate_vishing_script("Example Bank", "Bank Representative", "Suspicious Transaction",
    "Hello, this is Sam from the fraud department. We noticed an unusual/suspicious transaction.",
    "Please confirm the one-time verification code that was sent to your phone."
))

# 3. Government Scenario
print(generate_vishing_script("Example Public_Service", "Government Officer", "Identity Verification",
    "Hello, this is Noah from a public-service office. We need to verify information related to your account.",
    "This verification must be completed within the next 12 hours to avoid delays with your account. " \
    "Please provide your personal identification details so we can complete the process."))