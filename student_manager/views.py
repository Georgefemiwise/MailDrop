from rest_framework.decorators import api_view
from rest_framework.response import Response


from student_manager.builder import (
    create_student_for_btech_diptech,
    create_student_for_hnd,
)
from student_manager.serializers import StudentSerializer
from .models import Student
from .helper.utils import (
    is_valid_email_address,
)


@api_view(["GET"])
def create_student(request, index):
    if request.method != "GET":
        return Response({"error": "Unsupported method"}, status=405)

    if not is_valid_email_address(index):
        return Response({"error": "Invalid email address"}, status=400)

    student_index = index
    if len(student_index) != 10:
        return Response({"error": "Invalid index format or does not exist"}, status=400)

    if student_index[:2] in ["bc", "pd"] and student_index[2:5].isalpha():
        return create_student_for_btech_diptech(student_index)
    elif student_index.isdigit():
        return create_student_for_hnd(student_index)
    else:
        return Response({"error": "Invalid index format or does not exist"}, status=400)


@api_view(["GET"])
def all_students(request):
    """
    Retrieves all students from the database, serializes the data using a serializer, and
    returns the serialized data as a response.
    """

    if request.method == "GET":
        # Retrieve all students from the database
        students = Student.objects.all()

        # Serialize the data using the serializer
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=200)


@api_view(["GET"])
def count_students_in_course(request, course):
    if request.method == "GET":
        # Retrieve all students in the course
        students_in_course = Student.objects.filter(course=course)

        # Count the number of students in the course
        student_count = students_in_course.count()

        # You can return the count or other relevant information as needed
        return Response({"course": course, "student_count": student_count}, status=200)


@api_view(["GET"])
def count_students_in_year(request, year_enrolled):
    if request.method == "GET":
        # Retrieve all students in the course
        students_in_course = Student.objects.filter(year_enrolled=year_enrolled)

        # Count the number of students in the course
        student_count = students_in_course.count()

        # You can return the count or other relevant information as needed
        return Response(
            {"course": year_enrolled, "student_count": student_count}, status=200
        )


@api_view(["GET"])
def count_students_in_program(request, program):
    if request.method == "GET":
        program = program.upper()
        # Retrieve all students in the program
        students_in_program = Student.objects.filter(program=program)

        # Get the unique enrollment years of students in the program
        enrollment_years = students_in_program.values_list(
            "year_enrolled", flat=True
        ).distinct()

        # Count the number of students in the program
        student_count = students_in_program.count()

        # Return the count and enrollment years
        return Response(
            {
                "program": program,
                "student_count": student_count,
                "enrollment_years": list(enrollment_years),
            },
            status=200,
        )


@api_view(["GET"])
def count_students_graduating_in_year(request, year_enrolled):
    if request.method == "GET":
        # Retrieve all students in the course
        students_in_course = Student.objects.filter(year_enrolled=int(year_enrolled))

        # Count the number of students in the course
        student_count = students_in_course.count()

        # You can return the count or other relevant information as needed
        return Response(
            {"course": year_enrolled, "student_count": student_count}, status=200
        )


@api_view(["GET"])
def get_student_by_index(request, index):
    if request.method == "GET":
        # Retrieve student from the database
        student = Student.objects.get(index=index)

        # Serialize the data using the serializer
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data, status=200)
