from student_manager.constants import PROGRAMS, COURSES, YEARS
from student_manager.helper.builder import (
    create_student_for_btech_diptech,
    create_student_for_hnd,
)
from student_manager.helper.utils import generate_index_number, is_valid_email_address


def auto_create_student():
    """
    Automates the creation of students based on predefined constants.

    Iterates over the specified years, programs, and courses to generate student indices
    and creates students for each index based on the program type.

    `Note: The created students are based on a default index number.`

    Returns:
    - None
    """
    default_index_number = 200

    for year in YEARS:
        for program_code in PROGRAMS.values():
            for course_code in COURSES.values():
                index = generate_index_number(
                    program=program_code,
                    course=course_code,
                    _year_enrolled=year,
                    index=default_index_number,
                )

                if is_valid_email_address(index):
                    # If the program is HND, create a student for HND; otherwise, for BTECH/DIPTECH
                    if program_code == "07":
                        create_student_for_hnd(index)
                    else:
                        create_student_for_btech_diptech(index)


