from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.shortcuts import render
from datetime  import datetime



def index(request):
     
     return HttpResponse('Hello world this is my first shit')


def createStudentDetails(request):
    thisYear = datetime.now().year
    
    
    
    if request.method == 'POST':
        program = request.POST['program']
        level = request.POST['level']
        year = request.POST['year']
        totalInClass = 16
        
        if year is None and year > thisYear:
            print('errro year: %s is greater than %s' % year, thisYear )
            
        else:
            

            for index in range(1, totalInClass):
                generatedEmail = f"{program}{str(year)}{index:03}@ttu.edu.gh"

                # Check if the object does not already exist
                if not Student.objects.filter(email=generatedEmail).exists():
                    # Save the object to the database
                    newStudent = Student.objects.create(
                        index = index,
                        program = program,
                        email = generatedEmail,
                        level = level,
                        year_enrolled = year,
                    )
                    newStudent.save()  
                    
                    
                    # Check for form validation errors
                    if newStudent.pk is None:
                        print(newStudent.errors)
    return render(request, 'templates/index.html')



# function to get all student

def getAllStudentDetails(request):
     
     
     allStudent = Student.objects.all().count()
     return HttpResponse('getting student details {0} s'.format(allStudent))


# def getEmail(*args):
#      args = Student.objects.filter(args=args)
#      return args
# print(getEmail('abc'))
