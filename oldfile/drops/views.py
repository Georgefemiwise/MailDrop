from django.shortcuts import render
from .dropAds import DropAddress


#email messages import-----------
from django.conf import settings
from django.core import mail
#----------------------------------

#forms, models imported-----------------------------
from .models import test as Test ,BachelorsDegreeAddresses as BDA
from .forms import EmailForm
#----------------------------------



# home page rendering function
def home(request): 
     #collect values from the html inputs
     if request.method == 'POST':
          number = request.POST['number']
          program = request.POST['program']
          year = request.POST['year']

     #refers to the class it called from (DropAddress)
          address = DropAddress(numInClass=number,program=program,year=year)
          address.genAddress()

     return render (request, 'templates\index.html')




def emailer(request):
     if request.method == 'POST':
          form = EmailForm(request.POST)

          if form.is_valid():
               subject = form.cleaned_data['subject']
               message = form.cleaned_data['message']
               

               recievers = []#list of email from the database
               for person in Test.objects.all():
                    recievers.append(person.address)

               from_email =settings.EMAIL_HOST_USER
               connection = mail.get_connection()

               # Manually open the connection
               connection.open() 

               # Construct an email message that uses the connection
               email_messages = mail.EmailMessage(
                    subject =  subject.capitalize(),
                    from_email = from_email,
                    body = message,
                    to = recievers,
                    connection = connection,
                    )

               # email_messages.send()   <<--- to send a single message
#-----------------------------------------------------------------------------------------------               
               connection.send_messages([email_messages]) #to send multiple messages
                
               # Manually close the connection
               connection.close()

 

     else:
          form = EmailForm()

     return render(request,'emailer.html', {'form': form})


