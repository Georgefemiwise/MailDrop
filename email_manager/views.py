from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import render

def send_email_to_student(request,sender: str, password: str, recipients: list):
    """Send email messages to student. """
    
    
   
    subject = 'Subject of your email'
    message_body = 'This is the body of your email.'

    # Create an EmailMessage object
    email = EmailMessage(subject=subject, body=message_body, from_email=sender_email, to=recipients,)

    # Attach a file (change the file path to your attachment)
    file_path = 'path/to/your/attachment.pdf'
    email.attach_file(file_path)

    try:
        email.send()
        return render(request, 'success.html', {'message': 'Email sent successfully'})
    except Exception as e:
        return render(request, 'error.html', {'message': f'Email sending failed: {e}'})
