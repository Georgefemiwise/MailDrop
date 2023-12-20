from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import get_key_by_value
from .models import Student
from .serializers import StudentSerializer


# major school programs
PROGRAMS = {"BTECH": "BC", "DIPTECH": "DP", "HND": "07"}


@api_view(["GET"])
def all_student(request):
    if request.method == "GET":
        # Retrieve all students from the database
        students = Student.objects.all()
        print(students)
        # Serialize the data using the serializer
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=200)


@api_view(["GET"])
def last_index(request, index):
    if request.method == "GET":
        
        student_index = index
        if index:
            if ("bc" in student_index) or ("pd" in student_index):
                for index in range(1, int(student_index[7:]) + 1):
                    # convert index into relevant data
                    course = student_index[2:-5]
                    program = get_key_by_value(PROGRAMS, student_index[:-8])  # bc
                    year_enrolled = f"20{student_index[5:-3]}"
                    index = f"{index:3}"

                    # Create a single student with the provided index
                    Student.objects.create(
                        index=index,
                        course=course,
                        program=program,
                        year_enrolled=year_enrolled,
                    )

            return Response({"sucess": ""}, status=201)
        else:
            # Handle the case where the index is not combination of course and program and date
            return Response({"error": "Invalid index format"}, status=400)

    return Response({"error": "Unsupported method"}, status=405)


