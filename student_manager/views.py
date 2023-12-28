from rest_framework.decorators import api_view
from rest_framework.response import Response


from .constants import *
from .helper.utils import *
from .models import Student
from .serializers import StudentSerializer


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
def create_student(request, index):
    """
    This function checks if the last student's index, validated through their email address, exists.
    If it does, the function creates a student object with the
    relevant data by looping throught the range of the index backwards to the first.

    """

    if request.method == "GET":  # todo change to PUT
        student_index = index  # index is obtained from the request

        # Validate if the index exists through an email check
        is_valid = is_email_address_exists(index)
        # is_valid = True  # for dev sake only to limit request to the api

        if is_valid:
            if len(student_index) == 10:
                # Check if it's a valid format for index (e.g., bcict21064)
                if (
                    # Handle BTECH & DIPTECH requests
                    student_index[:2] in ["bc", "pd"]
                    and student_index[2:5].isalpha()
                    and student_index[5:7].isdigit()
                    and student_index[7:].isdigit()
                ):
                    for index in range(1, int(student_index[7:]) + 1):
                        # Convert index into relevant data
                        get_course = student_index[2:-5]
                        get_program = get_key_by_value(PROGRAMS, student_index[:-8])
                        get_year_enrolled = f"20{student_index[5:-3]}"
                        get_index = generate_index_number(
                            PROGRAMS.get(get_program),
                            index,
                            get_year_enrolled[2:],
                            get_course,
                        )

                        check_existence = Student.objects.filter(
                            index=get_index, program=get_program
                        )
                        if check_existence.exists():
                            continue

                        # get a generated email
                        get_email = generate_email(
                            index=index,
                            year=get_year_enrolled,
                            course=get_course,
                            program=PROGRAMS.get(get_program),
                        )
                        # calculate the graduation year  for the student
                        get_graduation_data = cal_graduation_date(
                            PROGRAMS.get(get_program), get_year_enrolled
                        )

                        # Create a single student with the provided index
                        Student.objects.create(
                            index=get_index,
                            email=get_email,
                            course=get_course,
                            program=get_program,
                            year_enrolled=get_year_enrolled,
                            graduation_year=get_graduation_data,
                        )

                    return Response(
                        {"success": "Successfully created"},
                        status=201,
                    )

                # Handle HND requests
                elif len(student_index) == 10 and student_index.isdigit():
                    # todo   should perform a loop to populate the student info for HND

                    for index in range(1, int(student_index[7:]) + 1):
                        get_index = generate_index_number()

                        # get a generated email
                        get_email = generate_email(
                            index=index,
                            year=get_year_enrolled,
                            course=get_course,
                            program=PROGRAMS.get(get_program),
                        )
                        

                        # Create a single student with the provided index
                        Student.objects.create(
                            index=get_index,
                            email=get_email,
                            course=get_course,
                            program=get_program,
                            year_enrolled=get_year_enrolled,
                            graduation_year=get_graduation_data,
                        )
                    return Response({student_index})

            else:
                # Handle the case where the index format is invalid
                return Response(
                    {"error": "Invalid index format or does not exist"}, status=400
                )
        else:
            # Handle the case where the email check fails
            return Response({"error": "Invalid email address"}, status=400)

    return Response({"error": "Unsupported method"}, status=405)


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
