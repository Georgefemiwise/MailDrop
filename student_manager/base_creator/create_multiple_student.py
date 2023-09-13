r"""this module is responsible for generating multiple instances of students data."""

import time

from apscheduler.schedulers.background import BackgroundScheduler

from .create_student import create_single_student
from ..models import Program, Department


def start_creation():
    """Starts the scheduler function in the background tp populate new student """

    # initialize scheduler class
    scheduler = BackgroundScheduler()

    # add function to run in the background and set timer ['interval', 'date']
    scheduler.add_job(create_multiple_students, "interval", seconds = 5)

    # # start the process
    scheduler.start()


def create_multiple_students():
    r""" Create multiple student within a range number of student.

     Assuming there are 50 student in a class, by specifying in the 'range_of_student' variable it should be able to
     create this range of student with the required detail provided it is given. """

    # states the current year in string
    current_year = time.strftime('%Y')

    # range of student to be generated
    range_of_students = 3

    # get department from the database
    list_of_departments = Department.objects.all()
    list_of_programs = Program.objects.all()

    print("Creating students...")

    count = 0
    for department in list_of_departments:

        # # getting the list of departments
        get_department_abbreviation = department.department_abbreviation

        for program in list_of_programs:

            # # extracting program abbreviation
            program_abbreviation = program.program_abbreviation

            for index in range(1, range_of_students + 1):
                create_single_student(
                    program_name = program.program_name,
                    program_abbreviation = program_abbreviation,
                    department_abbreviation = get_department_abbreviation,
                    index_number = index,
                    year_enrolled = current_year
                )

                count += index

    print(f"{count} students created!")
    return True
