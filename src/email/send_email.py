from core import sender
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


# Email configuration
file = "src/email/messages.txt"
with open(file, "r") as f:
    lines = f.read()
    lines = lines.split("\n")
    subject = lines[0].replace("Subject: ", "")
    content = "\n".join(lines[1:])

# Access specific variables
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")


# list of recipient
recipient_email = ["allprowise@gmail.com", "bcict21064@ttu.edu.gh"]


# send the email
sender(sender_email, sender_password, recipient_email, subject, content)
