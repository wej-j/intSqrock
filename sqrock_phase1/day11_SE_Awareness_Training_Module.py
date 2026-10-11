import json

QUESTIONS = [
    {
        "q": "An email asks you to verify your password via a link. You should:",
        "opts": ["A) Click the link","B) Call IT directly","C) Reply with password"],
        "ans": "B",
        "exp": "Always verify via official channels, never click email links."
    },
    {
        "q": "You find a USB drive in the parking lot. You should:",
        "opts": ["A) Plug it in to check","B) Hand to security","C) Keep it"],
        "ans": "B",
        "exp": "USB drops are a classic baiting attack vector."
    },
    {
        "q": "You receive a connection request from an account using your colleague's name and photo, but the username is slightly different. What should you do?",
        "opts": [
            "A) Accept it because the name and photo look familiar",
            "B) Verify the account with your colleague through another trusted channel",
            "C) Send the account your personal information to confirm their identity"
        ],
        "ans": "B",
        "exp": "Impersonation accounts may copy names and profile photos. Verify suspicious accounts through a trusted channel before interacting with them."
    },
    {
        "q": "You visit a website you normally trust, but it suddenly asks you to download an unexpected software update. What should you do?",
        "opts": [
            "A) Download it immediately because the website is familiar",
            "B) Avoid the download and verify the update through the official software source",
            "C) Disable the browser security warning and continue"
        ],
        "ans": "B",
        "exp": "Trusted websites can sometimes be compromised in watering-hole attacks. Unexpected downloads should be verified through an official source."
    },
    {
        "q": "Someone claiming to be from IT calls and asks for your current password. What should you do?",
        "opts": ["A) Give the password because IT asked for it","B) Refuse and verify the request through official IT channels","C) Give only part of the password"],
        "ans": "B",
        "exp": "Legitimate IT staff should not ask users to reveal their passwords."
    },

    {
        "q": "You receive an urgent SMS saying your account will be closed unless you click a link immediately. What is this most likely an example of?",
        "opts": ["A) Smishing","B) OSINT","C) Patch management"],
        "ans": "A",
        "exp": "Smishing is SMS-based phishing and often uses urgency to encourage users to click links."
    },
    {
        "q": "Which of the following is a warning sign that a social-media profile may be fake?",
        "opts": ["A) A very new account with very few posts","B) An old account with regular activity","C) A complete profile with a normal follower ratio"],
        "ans": "A",
        "exp": "A new account with little activity can be one of several indicators of a fake or bot profile."
    },
    {
        "q": "A caller says they are from your bank and asks you to read out a one-time verification code. What should you do?",
        "opts": ["A) Give them the code","B) End the call and contact the bank through an official number","C) Send the code by SMS instead"],
        "ans": "B",
        "exp": "Verification codes should not be shared during unexpected calls. The request should be verified independently."
    },
    {
        "q": "Which security measure can help reduce repeated automated login attempts?",
        "opts": ["A) Rate limiting","B) Publishing more account information","C) Disabling passwords"],
        "ans": "A",
        "exp": "Rate limiting restricts repeated login attempts and can help reduce brute-force or dictionary-style attacks."
    },
    {
        "q": "Which information should generally be limited when using public developer or social-media profiles?",
        "opts": ["A) Unnecessary personal and organizational information","B) Only programming languages","C) Nothing, because public information cannot be misused"],
        "ans": "A",
        "exp": "Public information can contribute to an OSINT profile, so unnecessary personal or organizational details should be limited."
    },
    {
        "q": "Which action can help reduce the risk of watering-hole attacks?",
        "opts": ["A) Web filtering and keeping software patched","B) Clicking unfamiliar download links","C) Disabling browser security features"],
        "ans": "A",
        "exp": "The internship guidance lists web filtering, script blocking, and patch management as defenses against watering-hole attacks."
    },
    {
        "q": "You receive a personalized email that mentions your company and location and asks you to verify your account urgently. What should you do?",
        "opts": ["A) Trust it because it contains personal information","B) Verify the request through an official channel before taking action","C) Forward your credentials to confirm your identity"],
        "ans": "B",
        "exp": "Spear-phishing messages may use public information to appear convincing, so unexpected requests should be independently verified."
    }
]

def run_quiz():
    score = 0
    answers = []
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}: {q['q']}")
        for o in q["opts"]:
            print(f" {o}")
        ans = input("Your answer (A/B/C): ").strip().upper()
        # Check if the answer is correct
        if ans == q["ans"]:
            print("Correct!")
            score += 1
            correct = True
        else:
            print(f"Wrong. {q['exp']}")
            correct = False
        # Save the answer
        answers.append({
            "question_number": i,
            "question": q["q"],
            "your_answer": ans,
            "correct_answer": q["ans"],
            "correct": correct,
            "explanation": q["exp"]
        })
    print(f"\nScore: {score}/{len(QUESTIONS)}")

    # Create the final result
    result = {
        "score": score,
        "total_questions": len(QUESTIONS),
        "answers": answers
    }

    # Save everything to JSON
    with open("quiz_score.json", "w") as f:
        json.dump(result, f, indent=4)

    print("\nQuiz results saved to quiz_score.json")


run_quiz()