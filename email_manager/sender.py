# import smtplib
# import datetime
# import time
# from django.core.mail import EmailMessage

# # Set up SMTP connection
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# sender_email = 'sender@gmail.com'
# sender_password = 'sender_password'
# recipient_email = 'recipient@example.com'

# # Send message every Saturday
# while True:
#     today = datetime.datetime.today()
#     if today.weekday() == 5: # Saturday
#         subject = 'Weekly update'
#         body = 'Hello,\n\nThis is your weekly update.\n\nBest regards,\nSender'
#         email = EmailMessage(subject, body, sender_email, [recipient_email])
#         email.send(fail_silently=False)
#         print(f'Message sent to {recipient_email} on {today}.')
#         time.sleep(86400) # wait for 24 hours
#     else:
#         time.sleep(3600) # wait for 1 hour



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'
subject = 'Subject of your email'
message_body = 'This is the body of your email.'

# Create a MIMEText object to represent the email content
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject

# Attach the plain text message body
message.attach(MIMEText(message_body, 'plain'))

# Attach an image (change the file path to your image)
image_path = 'path/to/your/image.jpg'
with open(image_path, 'rb') as img_file:
    img = MIMEImage(img_file.read())
    img.add_header('Content-Disposition', 'attachment', filename='image.jpg')
    message.attach(img)

# Establish an SMTP connection and send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()  # Start a TLS/SSL secured connection
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, message.as_string())
    print('Email with image sent successfully')
except smtplib.SMTPException as e:
    print('Email sending failed:', e)
