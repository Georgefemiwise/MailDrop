import logging
from student_manager.constants import PROGRAMS
from student_manager.helper.utils import (
    cal_graduation_date,
    generate_email,
    generate_index_number,
    get_key_by_value,
)
from rest_framework.response import Response
from student_manager.models import Student


# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="created_students.log",
    filemode="w",
)
logger = logging.getLogger(__name__)


def create_student_for_btech_diptech(student_index, auto_create_student=False):
    program = student_index[:2]
    course = student_index[2:-5]
    year_enrolled = f"20{student_index[5:-3]}"

    num_students = int(student_index[7:])
    for index in range(1, num_students + 1):
        create_single_student(
            program=program, course=course, year_enrolled=year_enrolled, index=index
        )
    # Log a success message
    logger.info(f"Successfully created  {num_students} {program} students")
    return (
        Response({"success": "Successfully created"}, status=201)
        if not auto_create_student
        else None
    )


def create_student_for_hnd(student_index, auto_create_student=False):
    program = student_index[:2]

    year_enrolled = student_index[2:4]
    num_students = int(student_index[7:])
    for index in range(1, num_students + 1):
        create_single_student(program=program, year_enrolled=year_enrolled, index=index)

    # Log a success message
    logger.info(f"Successfully created {num_students} {program} students")
    return (
        Response({"success": "Successfully created"}, status=201)
        if not auto_create_student
        else None
    )


def create_single_student(program, year_enrolled, index, course=None):
    """
    The function creates a single student object with the given program, year enrolled, index, and
    optional course.
    """

    get_index = generate_index_number(program, index, year_enrolled, course)
    check_existence = Student.objects.filter(
        index=get_index, program=program, year_enrolled=year_enrolled
    )
    if check_existence.exists() == False:
        get_email = generate_email(index=get_index)
        program = get_key_by_value(program)
        get_graduation_data = cal_graduation_date(program, year_enrolled)

        print(check_existence.exists(), get_email)
        Student.objects.create(
            index=get_index,
            email=get_email,
            course=course if course is not None else "unknown",
            program=program,
            year_enrolled=year_enrolled,
            graduation_year=get_graduation_data,
        )
    else:
        pass
