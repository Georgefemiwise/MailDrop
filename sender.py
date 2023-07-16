import smtplib
import datetime
import time
from django.core.mail import EmailMessage

# Set up SMTP connection
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'sender@gmail.com'
sender_password = 'sender_password'
recipient_email = 'recipient@example.com'

# Send message every Saturday
while True:
    today = datetime.datetime.today()
    if today.weekday() == 5: # Saturday
        subject = 'Weekly update'
        body = 'Hello,\n\nThis is your weekly update.\n\nBest regards,\nSender'
        email = EmailMessage(subject, body, sender_email, [recipient_email])
        email.send(fail_silently=False)
        print(f'Message sent to {recipient_email} on {today}.')
        time.sleep(86400) # wait for 24 hours
    else:
        time.sleep(3600) # wait for 1 hour

# python -m venv env
# env/Scripts/.\Activate.ps1
# cd ..
# cd ..
# pip install django  djangorestframework

# django-admin startproject maildrop
# cd maildrop
# code .

