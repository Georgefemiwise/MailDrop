from django.shortcuts import render
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Student, Department,Program
from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .serializers import StudentSerializer, ProgramSerializer





@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
         # Extract data from the serializer
        level = serializer.validated_data.get('level')
        year = serializer.validated_data.get('year_enrolled')
        classTotal = int(request.data.get('classTotal'))
        program_data = serializer.validated_data.get('program')
        program_name = program_data.get('abbreviation') if program_data else None

        # convert class to interger
        classTotal = int(classTotal) 
      
        thisYear = datetime.now().year

        if year and year > thisYear:
            error_message = 'Error: year {} is greater than {}'.format(year, thisYear)
            return Response({'error': error_message}, status=400)

        if program_name:
            for index in range(1, classTotal + 1):
                generatedEmail = f"{program_name}{str(year)[2:]}{index:03}@ttu.edu.gh"
                print(f"Processing student with email: {generatedEmail} on {index}")
                
                
                if not Student.objects.filter(email=generatedEmail).exists():
                    program = get_object_or_404(Program, abbreviation__iexact=program_name)
                    print(f"Creating student with email: {generatedEmail}")

                    newStudent = Student(
                        index=f"{index:03}", #leading zero for index numbers
                        program=program,
                        email=generatedEmail.lower(),
                        level=level,
                        year_enrolled=year,
                    )
                    newStudent.save()
                    print(f"{generatedEmail} created")

                    if newStudent.pk is not None:
                        success_message = 'Student created successfully'
                        # return Response({'message': success_message}, status=201)

            error_message = 'Error saving the student'
            # return Response({'error': error_message}, status=500)

        error_message = 'Program data is required.'
        return Response({'error': error_message}, status=400)

    return Response(serializer.errors, status=400)



            
  
@api_view(['GET'])
def get_student(request, student_index):
    student = get_object_or_404(Student, id=student_index)
    serializer = StudentSerializer(student, many=False)
    
    # Retrieve the serialized data
    serialized_student = serializer.data
    
    # Serialize the associated Program object
    program_serializer = ProgramSerializer(student.program)
    serialized_program = program_serializer.data
    
    # Add serialized Program to the student data
    serialized_student['program'] = serialized_program
    
    # Add other student details to the serialized data
    serialized_student['level'] = student.level
    serialized_student['year'] = student.year_enrolled
    serialized_student['index'] = student.index
    serialized_student['email'] = student.email
    
    return Response(serialized_student)

    
@api_view(['GET'])
def get_all_departments(request):
    if request.method == 'GET':
        departments = Department.objects.all().values('id', 'name')
        return Response(departments)
    
    
@api_view(['GET'])
def get_all_programs(request):
    if request.method == 'GET':
        programs = Program.objects.all().values('id', 'name', 'abbreviation')
        return Response(programs)


@api_view(['GET'])
def students_in_program(request, programID):
    if request.method == 'GET':
        students = Student.objects.filter(program=programID)
        serializer = StudentSerializer(students, many=True)

        # Retrieve the serialized data
        serialized_students = serializer.data

        # Add email and index fields to each student
        for student_data in serialized_students:
            student = Student.objects.get(id=student_data['id'])
            program = student.program
            program_data = {
                'name': program.name,
                'department': program.department.name
            }
            student_data['program'] = program_data
            student_data['email'] = student.email
            student_data['index'] = student.index

        # Return the updated serialized students as a response
        return Response(serialized_students)

        

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





test = 'hi my name is '.format('gee')
print(test)
