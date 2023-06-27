from django.shortcuts import render
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Student
from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .serializers import StudentSerializer, ProgramSerializer



def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        program = serializer.validated_data['program']
        level = serializer.validated_data['level']
        year = serializer.validated_data['year_enrolled']
        numInClass = serializer.validated_data['classTotal']
        
        thisYear = datetime.now().year

        if year > thisYear:
            error_message = 'Error: year {} is greater than {}'.format(year, thisYear)
            return Response({'error': error_message}, status=400)
        

        for index in range(1, numInClass):
            generatedEmail = f"{program}{year}{index:03}@ttu.edu.gh"

            if not Student.objects.filter(email=generatedEmail).exists():
                newStudent = Student(
                    index=index,
                    program=program,
                    email=generatedEmail,
                    level=level,
                    year_enrolled=year[2:],
                )
                newStudent.save()

                if newStudent.pk is None:
                    error_message = 'Error saving the student'
                    return Response({'error': error_message}, status=500)

        success_message = 'Student created successfully'
        return Response({'message': success_message}, status=201)

    return Response(serializer.errors, status=400)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer

@api_view(['GET'])
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        # Retrieve the serialized data
        serialized_students = serializer.data

        # Add program information to each student
        for student_data in serialized_students:
            student = Student.objects.get(id=student_data['id'])
            program = student.program
            program_data = {
                'name': program.name,
                'department': program.department.name
            }
            student_data['program'] = program_data

        # Return the updated serialized students as a response
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
