from osint_module import osint_scan
from profile_module import github_profile
from phish_module import phish_score
from template_module import awareness_email_template
from ir_module import ir_response


MODULES = {
    "1": "Passive OSINT Scanner",
    "2": "Public GitHub Profile",
    "3": "Phishing URL Scorer",
    "4": "Awareness Email Template",
    "5": "Incident Response Simulation",
    "0": "Exit"
}


def menu():
    while True:
        print("\n" + "=" * 45)
        print("     SOCIAL ENGINEERING CHAIN SIMULATOR     ")
        print("      Sqrock Cybersecurity Internship       ")
        print("=" * 45)

        for key, value in MODULES.items():
            print(f"[{key}] {value}")

        choice = input("\nSelect module: ").strip()

        if choice == "1":
            domain = input(
                "Enter practice/authorized domain "
                "(example.com): "
            ).strip()

            if not domain:
                domain = "example.com"

            osint_scan(domain)

        elif choice == "2":
            username = input(
                "Enter public GitHub username: "
            ).strip()

            github_profile(username)

        elif choice == "3":
            url = input(
                "Enter URL string to analyze: "
            ).strip()

            score = phish_score(url)

            print(f"\nRisk Score: {score}%")

        elif choice == "4":
            target = {
                "name": input("Fictional name: "),
                "email": input(
                    "Fictional email "
                    "(example.com recommended): "
                ),
                "location": input(
                    "Fictional location: "
                )
            }

            print(awareness_email_template(target))

        elif choice == "5":
            incident = {
                "type": input(
                    "Enter incident type (phishing, smishing, vishing, etc.): "
                ).strip().lower(),

                "severity": input(
                    "Enter severity (LOW, MEDIUM, HIGH, CRITICAL): "
                ).strip().upper(),

                "user": input(
                    "Enter fictional affected user: "
                ).strip()
            }

            ir_response(incident)

        elif choice == "0":
            print("\nExiting simulator.")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    menu()