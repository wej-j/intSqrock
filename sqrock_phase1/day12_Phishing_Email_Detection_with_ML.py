from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

emails = [
    # 5 original emails
    "Verify your account now or it will be suspended",
    "Click here to claim your prize immediatly",
    "Team standup at 3pm, agenda attached",
    "Your invoice for Q2 is ready dor review",
    "Urgent: update your bank details to avoid closure",
    ## 25 Phishing Emails
    "Verify your account immediately to avoid suspension",
    "Urgent: update your password within 24 hours",
    "Click this link to confirm your account details",
    "Your account has been locked, verify your identity now",
    "You have won a prize, click here to claim it",
    "Security alert: unusual login detected on your account",
    "Update your billing information to prevent service interruption",
    "Your mailbox storage is full, login now to increase capacity",
    "Confirm your bank information to avoid account closure",
    "Immediate action required: verify your login credentials",
    "We detected suspicious activity, reset your password now",
    "Your payment failed, update your card information immediately",
    "Click here to unlock your account",
    "Important security notice: confirm your identity today",
    "Your account will expire unless you verify it now",
    "You have received a refund, click here to collect it",
    "Login required to review suspicious account activity",
    "Verify your email address to prevent account deactivation",
    "Urgent payment request: confirm your banking details",
    "Your password has expired, update it using this link",
    "You have been selected for a special reward, claim it now",
    "Account warning: login immediately to secure your profile",
    "Confirm your personal information to restore account access",
    "Your subscription will be cancelled unless you update payment details",
    "Security team alert: verify your credentials immediately",
    ## 25 Legitimate Emails
    "Team meeting is scheduled for tomorrow at 10am",
    "Please find the project notes attached for review",
    "Your monthly report is ready for review",
    "Reminder: department meeting this Friday afternoon",
    "Thank you for attending today's training session",
    "The project deadline has been moved to next Monday",
    "Please review the attached meeting agenda before tomorrow",
    "Lunch with the team is scheduled for 12:30",
    "Here are the notes from yesterday's meeting",
    "Your requested document has been uploaded to the shared folder",
    "The development team completed the latest software update",
    "Please send your feedback on the new project proposal",
    "Reminder to submit your weekly progress report",
    "The office will be closed next Monday for the holiday",
    "Your support request has been received and assigned",
    "The quarterly team presentation is available for review",
    "Please review the attached invoice for the completed project",
    "The training session will begin at 2pm tomorrow",
    "Your calendar invitation for the workshop has been sent",
    "The project files have been updated in the shared workspace",
    "Thank you for submitting your application",
    "Your scheduled appointment is confirmed for Friday",
    "Please review the minutes from today's team discussion",
    "The latest documentation is available in the project folder",
    "The weekly team standup will begin at 9am"
]
labels = [1, 1, 0, 0, 1,
          1, 1, 1, 1, 1,
          1, 1, 1, 1, 1,
          1, 1, 1, 1, 1,
          1, 1, 1, 1, 1,
          1, 1, 1, 1, 1,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0, 0 ]  # 1:phishing, 0:legit

pipe = Pipeline([("vec", CountVectorizer()), ("clf", MultinomialNB())])
X_train, X_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.35,
    random_state=42,
    stratify=labels
)
pipe.fit(X_train, y_train)
predictions = pipe.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion matrix
print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, predictions)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Legitimate", "Phishing"]
)
disp.plot()
plt.title("Confusion Matrix")
plt.show()

# Classification report
print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=["Legitimate", "Phishing"]
))


# Optional extra tests
tests = [
    "Please verify your PayPal login",
    "Meeting notes from yesterday"
]

print("\nExtra Test Emails:")

for t in tests:
    pred = pipe.predict([t])[0]
    print(f"{'PHISHING' if pred else 'LEGIT'}: {t}")