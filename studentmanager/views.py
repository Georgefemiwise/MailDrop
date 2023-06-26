from django.shortcuts import render
from datetime import datetime
from django.shortcuts import get_object_or_404


from .models import Student
from .forms import StudentForm
import json
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def create_student(request):
    thisYear = datetime.now().year

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            program = form.cleaned_data['program']
            level = form.cleaned_data['level']
            year = form.cleaned_data['year_enrolled']
            totalInClass = 16

            if year > thisYear:
                error_message = 'Error: year {} is greater than {}'.format(year, thisYear)
                messages.error(request, error_message)
                return redirect('index')

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
                        error_message = 'Error saving the student'
                        messages.error(request, error_message)
                        return redirect('index')

            success_message = 'Student created successfully'
            messages.success(request, success_message)
            return redirect('index')

        else:
            errors = json.loads(form.errors.as_json())
            for field, field_errors in errors.items():
                for error in field_errors:
                    messages.error(request, error['message'])
            return redirect('index')


@api_view(['GET'])
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()

        # Serialize the students into JSON format
        serialized_students = [{'program': student.program,
                                'level': student.level,
                                'year': student.year_enrolled,
                                'id': student.id,
                                'index':student.index,
                                'email': student.email
                                } for student in students]

        # Return the serialized students as a response
        return Response(serialized_students)
    
@api_view(['GET'])
def get_student(request, student_index):
    student = get_object_or_404(Student, index=student_index)  # Or use index=student_id depending on your requirement

    # Serialize the student into JSON format or use a serializer
    serialized_student = {
        'program': student.program,
        'level': student.level,
        'year': student.year_enrolled,
        'id': student.id,
        'index': student.index,
        'email': student.email
    }

    # Return the serialized student as a response
    return Response(serialized_student)

@api_view(['PUT'])
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'PUT':
        program = request.data.get('program')
        level = request.data.get('level')
        year = request.data.get('year')

        # Update the student's attributes
        # Your code for updating the student goes here

        # Return a success response
        return Response({'message': 'Student updated successfully'})

    # Return an error response for invalid request methods
    return Response({'error': 'Invalid request method'})


@api_view(['DELETE'])
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'DELETE':
        # Delete the student from the database
        student.delete()

        # Return a success response
        return Response({'message': 'Student deleted successfully'})

    # Return an error response for invalid request methods
    return Response({'error': 'Invalid request method'})
