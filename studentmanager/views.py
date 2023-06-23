from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from .models import Student
from .form import StudentForm


def index(request):
    return render(request, 'index.html')

def create_student(request):
    thisYear = datetime.now().year

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            program = form.cleaned_data['program']
            level = 200  # Hardcoded level value for now
            year = form.cleaned_data['year_enrolled']
            totalInClass = 16

            if year > thisYear:
                error_message = 'Error: year {} is greater than {}'.format(year, thisYear)
                return JsonResponse({'error': error_message})

            for index in range(1, totalInClass):
                generatedEmail = f"{program}{year}{index:03}@ttu.edu.gh"

                if not Student.objects.filter(email=generatedEmail).exists():
                    newStudent = Student(
                        index=index,
                        program=program,
                        email=generatedEmail,
                        level=level,
                        year_enrolled=year,
                    )
                    newStudent.save()

                    if newStudent.pk is None:
                        return JsonResponse({'error': 'Error saving the student'})

            return JsonResponse({'message': 'Student created successfully'})

        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': errors})

    else:
        form = StudentForm()

    return render(request, 'index.html', {'form': form})



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
