EMAIL_HOST_PASSWORD = "twtkvyihjsvvnwyb"
EMAIL_HOST_USER = "maildrops.fun@gmail.com"


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# Email configuration
sender_email = EMAIL_HOST_USER
sender_password = EMAIL_HOST_PASSWORD
recipient_email = "allprowise@gmail.com"
subject = "Subject of your email"
message_body = "This is the body of your email."

# Create a MIMEText object to represent the email content
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# Attach the plain text message body
message.attach(MIMEText(message_body, "plain"))

# Attach an image (change the file path to your image)
image_path = "/home/george/Pictures/1 cdszV75g71so_OCZdI54Qg.png"
with open(image_path, "rb") as img_file:
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
