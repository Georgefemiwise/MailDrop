from django.shortcuts import render
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Student, Department,Program
from django.shortcuts import redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .serializers import StudentSerializer, ProgramSerializer




@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        level = serializer.validated_data['level']
        year = serializer.validated_data['year_enrolled']
        classTotal = request.data.get('classTotal')
        
        program_data = serializer.validated_data['program']
        program_name = program_data.get('name').lower()

        thisYear = datetime.now().year

        if year > thisYear:
            error_message = 'Error: year {} is greater than {}'.format(year, thisYear)
            return Response({'error': error_message}, status=400)
        
        for index in range(1, int(classTotal) + 1):
            generatedEmail = f"{program_name}{str(year)[2:]}{index:03}@ttu.edu.gh"

            if not Student.objects.filter(email=generatedEmail).exists():
                # Retrieve the Program instance from the database
                program = get_object_or_404(Program, name__iexact=program_name.lower())
                
                newStudent = Student(
                    index=index,
                    program=program,
                    email=generatedEmail.lower(),
                    level=level,
                    year_enrolled=year,
                )
                newStudent.save()

                if newStudent.pk is None:
                    error_message = 'Error saving the student'
                    return Response({'error': error_message}, status=500)

        success_message = 'Student created successfully'
        return Response({'message': success_message}, status=201)

    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
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
        programs = Program.objects.all().values('id', 'name')
        return Response(programs)


# Todo: Implement this method to get the list of students that are associated with a program
# @api_view(['GET'])
# def students_in_program(request, program):
#        if request.method == 'GET':
#         students = Student.objects.count(program=program)
#         serializer = StudentSerializer(students, many=True)

#         # Retrieve the serialized data
#         serialized_students = serializer.data

#         # Add email and index fields to each student
#         for student_data in serialized_students:
#             student = Student.objects.get(id=student_data['id'])
#             program = student.program
#             program_data = {
#                 'name': program.name,
#                 'department': program.department.name
#             }
#             student_data['program'] = program_data
#             student_data['email'] = student.email
#             student_data['index'] = student.index

#         # Return the updated serialized students as a response
#         return Response(serialized_students)

        
    



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
