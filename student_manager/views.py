from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import *
from .models import Student
from .api.api import is_email_address_exists
from .serializers import StudentSerializer


# major school programs
PROGRAMS: dict = {"BTECH": "BC", "DIPTECH": "DP", "HND": "07"}
COURCES = {"computer science": "ict"}


@api_view(["GET"])
def all_student(request):
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
def last_index(request, index):
    """
    This function checks if the last student's index, validated through their email address, exists.
    If it does, the function creates a student object with the
    relevant data by looping throught the range of the index backwards to the first.

    """

    if request.method == "GET":  # todo change to PUT
        student_index = index  # index is obtained from the request

        # Validate if the index exists through an email check
        is_valid = is_email_address_exists(index)
        # is_valid = True #for dev sake only to limit request to the api

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
                        get_index = f"{index:03}"

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
                        )

                    return Response(
                        {"success": "Successfully created"},
                        status=201,
                    )

                # Handle HND requests
                elif len(student_index) == 10 and student_index.isdigit():
                    # todo   should perform a loop to populate the student info for HND
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
