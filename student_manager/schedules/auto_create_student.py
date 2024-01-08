from student_manager.constants import PROGRAMS, COURSES, YEARS
from student_manager.helper.builder import (
    create_student_for_btech_diptech,
    create_student_for_hnd,
)
from student_manager.helper.utils import generate_index_number, is_valid_email_address


def auto_create_student():
    default = 200
    for year in YEARS:
        for program in PROGRAMS.values():
            for course in COURSES.values():
                index_number = default
                # Generate the index based on program, course, year, and index_number
                index = generate_index_number(
                    program=program,
                    course=course,
                    _year_enrolled=year,
                    index=index_number,
                )

                if is_valid_email_address(index):

                    # If the program is HND, create student for HND, else for BTECH/DIPTECH
                    if program == "07":
                        create_student_for_hnd(index, True)
                    else:
                        create_student_for_btech_diptech(index, True)

