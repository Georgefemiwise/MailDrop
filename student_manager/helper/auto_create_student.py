import random
from student_manager.constants import COURSES, PROGRAMS, YEARS


def auto_create_student(random_student_index):
    for year in YEARS:
        for program in PROGRAMS.keys():
            for course in COURSES.values():
                
                for index_number in range(1, random_student_index):
                    # Format the index based on the program type
                    if program == "HND":
                        index = f"{PROGRAMS[program]}{str(year)[2:]}{index_number:05d}"
                    else:
                        index = f"{PROGRAMS[program]}{course}{str(year)[2:]}{index_number:03d}"

                    print(index.lower())
                    print(course, program)


def gen_random_student_index():
    """"""
    default = 5
    # Test the function

    auto_create_student(default)
