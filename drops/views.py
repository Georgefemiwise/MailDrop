from django.shortcuts import render
from .models import Addresses
from schoolMailGenerator.generateEmailAddress import GenerateEmail

# Create your views here.


def home(request):
     class DropAddress(GenerateEmail):
          def __init__(self, program:str, year:int, numInClass:int):
               GenerateEmail.__init__(self, program, year)
               self.numInClass = numInClass

          def genAddress(self):
               for num in range(1,int(self.numInClass)+1):
                    generating = f"{self.program}/{str(self.year)}{num}@ttu.edu.gh"
                    address =Addresses.objects.create(Address=generating)
                    address.save()
 
     if request.method == 'POST':
          number = request.POST['number']
          program = request.POST['program']
          year = request.POST['year']

          address =DropAddress(numInClass=number,program=program,year=year)
          address.genAddress()




     return render (request, 'templates\index.html')