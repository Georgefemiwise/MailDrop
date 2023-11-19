import os
import json

from .core import sender
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


# Email configuration
file = "src/email/messages.txt"
with open(file, "r") as msg_file:
    lines = msg_file.read()
    lines = lines.split("\n")
    subject = lines[0].replace("Subject: ", "")
    content = "\n".join(lines[1:])

# Access specific variables
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

addressfile = "src/data/student_data.json"

with open(addressfile, "r") as address_file:
    x = json.load(address_file)

    # list of recipient
    recipient_email = [i["email"] for i in x]


def email_sender():
    """calls the email sender function"""

    # send the email
    sender(sender_email, sender_password, recipient_email, subject, content)
