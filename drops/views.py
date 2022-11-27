from django.shortcuts import render
from .models import Addresses
from schoolMailGenerator.generateEmailAddress import GenerateEmail

# Create your views here.

def emailer(program,year):
     return f"{program}{year}@ttu.edu.gh"




def home(request):
 
     if request.method == 'POST':
          number = request.POST['number']
          program = request.POST['program']
          year = request.POST['year']

          @GenerateEmail()




               # p?rogram=program, year=int(year)
          def classNumber(number):
               for num in range(1,number+1):
                    generating = f"{self.program}/{str(self.year)}/{num}@ttu.edu.gh"
               return generating


         
          address =Addresses.objects(classNumber())
          address.save()

          
         



     return render (request, 'templates\index.html')