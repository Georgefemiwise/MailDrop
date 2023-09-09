import time

from student_manager.models import Student, Program

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import StudentSerializer

CURRENT_YEAR = time.strftime('%Y')


@api_view(['GET'])
def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)

        # Retrieve the serialized data
        serialized_students = serializer.data

        # Add email and index fields to each student
        for student_data in serialized_students:
            student = Student.objects.get(id = student_data['id'])
            program = student.program
            program_data = {

                'abbreviation': program.program_abbreviation,
                'program_name': program.program_name,
                'department': program.department.department_name,
                'faculty': program.department.faculty.faculty_name,
            }
            student_data['program'] = program_data
            student_data['email'] = student.email
            student_data['index'] = student.index

        # Return the updated serialized students as a response
        return Response(serialized_students)
