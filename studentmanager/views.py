from .models import Student
from django.shortcuts import render
from datetime  import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def index(request):
     
     return render(request,'index.html')


# Create (POST request)
from datetime import datetime

def create_student(request):
    thisYear = datetime.now().year
    if request.method == 'POST':
        program = request.POST.get('program')
        level = request.POST.get('level')
        year = request.POST.get('year_enrolled')
        totalInClass = 16

        if year is None:
            return JsonResponse({'error': 'Year value is missing'})

        try:
            year = int(year)  # Convert year to integer
        except ValueError:
            return JsonResponse({'error': 'Invalid year value'})

        if year > thisYear:
            error_message = 'Error: year {} is greater than {}'.format(year, thisYear)
            return JsonResponse({'error': error_message})

        if program is None or program.strip() == "":
            return JsonResponse({'error': 'Program value is missing'})

        for index in range(1, totalInClass):
            generatedEmail = f"{program}{year}{index:03}@ttu.edu.gh"

            # Check if the object does not already exist
            if not Student.objects.filter(email=generatedEmail).exists():
                # Save the object to the database
                newStudent = Student(
                    index=index,
                    program=program,
                    email=generatedEmail,
                    level=level,
                    year_enrolled=year,
                )
                newStudent.save()

                # Check for form validation errors
                if newStudent.pk is None:
                    return JsonResponse({'error': 'Error saving the student'})

        # Return a success response
        return JsonResponse({'message': 'Student created successfully'})

    # Return an error response for invalid request methods
    return JsonResponse({'error': 'Invalid request method'})




# Read (GET request)
def get_all_students(request):
    if request.method == 'GET':
        Students = Student.objects.all()

        # Serialize the Students into JSON format
        serialized_Students = [{'program': Student.program, 'level': Student.level, 'year': Student.year_enrolled} for Student in Students]

        # Return the serialized Students as a response
        return JsonResponse(serialized_Students, safe=False)




# Update (PUT request)
def update_student(request, student_id):
    Student = get_object_or_404(Student, id=student_id)

    if request.method == 'PUT':
        program = request.POST.get('program')
        level = request.POST.get('level')
        year = request.POST.get('year')

        # Update the Student's attributes
        # Your code for updating the Student goes here

        # Return a success response
        return JsonResponse({'message': 'Student updated successfully'})
    
    # Return an error response for invalid request methods
    return JsonResponse({'error': 'Invalid request method'})



# Delete (DELETE request)
def delete_student(request, Student_id):
    Student = get_object_or_404(Student, id=Student_id)

    if request.method == 'DELETE':
        # Delete the Student from the database
        Student.delete()

        # Return a success response
        return JsonResponse({'message': 'Student deleted successfully'})
    
    # Return an error response for invalid request methods
    return JsonResponse({'error': 'Invalid request method'})
