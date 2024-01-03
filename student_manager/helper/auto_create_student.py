from student_manager.constants import PROGRAMS, COURSES, YEARS
from student_manager.builder import (
    create_student_for_btech_diptech,
    create_student_for_hnd,
)
from student_manager.helper.utils import generate_index_number


# def generate_student_index(program, course, year, index_number):
#     """
#     Generate a student index based on the given parameters.
#     """

#     if program == "HND":
#         return f"{PROGRAMS[program]}{str(year)[2:]}{index_number:05d}"
#     else:
#         return f"{PROGRAMS[program]}{course}{str(year)[2:]}{index_number:03d}"


def auto_create_student(last_student_index):
    for year in YEARS:
        for program in PROGRAMS.keys():
            for course in COURSES.values():
                for index_number in range(1, last_student_index + 1):
                    # Generate the index based on program, course, year, and index_number
                    index = generate_index_number(program=program, course=course, year=year, index=index_number)

                    # Check if the generated index is valid (add your validation logic here)
                    is_valid_index = True  # Replace with your validation logic

                    if is_valid_index:
                        # If the program is HND, create student for HND, else for BTECH/DIPTECH
                        if program == "HND":
                            create_student_for_hnd(index)
                        else:
                            create_student_for_btech_diptech(index)

                        # For testing purposes, print the generated index
                        print(index.lower())
                print("\n")


# Uncomment the line below to test the create_single_student function
# create_single_student("BTECH", "21", 1, "CSE")
