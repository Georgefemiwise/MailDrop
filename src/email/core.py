import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


def sender(
    sender_email=None,
    sender_password=None,
    recipient_email=None,
    subject="",
    content="",
    attachment_path=None,
):
    if sender_email is None or sender_password is None or recipient_email is None:
        return

    # Create a MIMEText object to represent the email content
   
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email if (len(recipient_email) <= 1) else ", ".join(recipient_email)
    message["Subject"] = subject

    # Attach the plain text message body
    message.attach(MIMEText(content, "plain"))

    # Attach an image if there is any
    if attachment_path is not None and os.path.isfile(attachment_path):
        with open(attachment_path, "rb") as img_file:
            img = MIMEImage(img_file.read())
            img.add_header("Content-Disposition", "attachment", filename="image.jpg")
            message.attach(img)

    # Establish an SMTP connection and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()  # Start a TLS/SSL secured connection
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, message.as_string())
        print("Email with image sent successfully")
    except smtplib.SMTPException as e:
        print("Email sending failed:", e)
