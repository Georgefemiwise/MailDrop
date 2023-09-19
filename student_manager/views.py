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

        list_students = []

        for student_data in serialized_students:
            list_students.append(dict(student = {

                "id": student_data['id'],
                "index": student_data["index"],
                "email": student_data["email"],

            }, status = {

                "level": student_data["level"],
                "inSchool": student_data["isInSchool"],
                "yearEnrollment": student_data["year_enrolled"],
                "graduation": student_data["graduation_date"],

            }, program = {

                "program": student_data["program"]["program_name"],
                "department": "departmentName",
                "faculty": "facultyName",

            }))

        return Response(list_students)
