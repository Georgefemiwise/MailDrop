from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


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
        if index.isnumeric():
            student_index = int(index)
            # Assuming you have other variables like course, program, and year_enrolled defined
            # Replace them with your actual data
            course = "YourCourse"
            program = "YourProgram"
            year_enrolled = 2023  # Replace with the actual year

            # Create a single student with the provided index
            Student.objects.create(
                index=student_index,
                course=course,
                program=program,
                year_enrolled=year_enrolled,
            )

            # Optionally, you can use the serializer to respond with the created student data
            created_student = Student.objects.get(index=student_index)
            serializer = StudentSerializer(created_student)
            return Response(serializer.data, status=201)
        else:
            # Handle the case where the index is not numeric
            return Response({"error": "Invalid index format"}, status=400)

    return Response({"error": "Unsupported method"}, status=405)



# bcict21064