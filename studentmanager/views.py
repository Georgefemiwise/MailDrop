from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.


def index(request):
     
     return HttpResponse('Hello world this is my first shit')


def createStudentDetails(request):
     if request.method == 'POST':
          index = request.POST['index']
          program = request.POST['program']
          email =  request.POST['email']
          level = request.POST['level']
          year = request.POST['year']
          totalInClass = 15 + 1
          
          # not sure about how many student in class but will render only 111
          for classNum in range(1,totalInClass):
               generatedEmail = f"{program}{str(year)}{classNum:03}@ttu.edu.gh"
               
               
               # check if the object dose not already
               if not Student.objects.filter(email = generatedEmail).exists(): 
                    
                    # save the objects to the database 
                    newEmail = Student.objects.create(email = generatedEmail, index = index, program = program, level = level, year = year,)
                    newEmail.save
              
   
     return HttpResponse('form')


def getStudentAllDetails(request):
     
     
     Student.objects.all()
     return HttpResponse('getting student details')


# def getEmail(*args):
#      args = Student.objects.filter(args=args)
#      return args
# print(getEmail('abc'))
