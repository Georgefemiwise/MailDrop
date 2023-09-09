import time
from ..models import Student, Program, Department
from apscheduler.schedulers.background import BackgroundScheduler

from django.shortcuts import get_object_or_404


def start():
    """Starts the scheduler function in the background tp populate new student """

    # initialize scheduler class
    scheduler = BackgroundScheduler()

    # add function to run in the background and set timer ['interval', 'date']
    scheduler.add_job(create_multiple_students, "interval", minutes = 2)

    # start the process
    scheduler.start()


def create_multiple_students():
    r""" Create multiple student within a range number of student.

     Assuming there are 50 student in a class, by specifying in the 'range_of_student' varialbe it should be able to create
     this range of student with the required detail provided it is given."""

    # states the current year in string
    current_year = time.strftime('%Y')

    # range of student to be generated
    range_of_students = 3

    # get programs from the database
    list_of_programs = Program.objects.all()

    print("Creating students...")

    for program in list_of_programs:
        # getting the list of programs
        get_program = Program.objects.get(program_name = program)

        # extracting program abbreviation
        program_abbreviation = get_program.program_abbreviation

        # extracting related department
        department = get_program.department.department_name

        for index in range(1, range_of_students + 1):
            create_single_student(program_name = program, program_abbreviation = program_abbreviation,
                                  department_name = department, index_number = index, year_enrolled = current_year)


def create_single_student(program_name: str, index_number: int, year_enrolled: str, program_abbreviation: str,
                          department_name: str):
    """
    Creates single student instance and the save to the database.
    """

    # get index number 
    full_index = generate_student_index(program = program_name, index = index_number, year = year_enrolled,
                                        program_abbreviation = program_abbreviation, department = department_name)

    # gets email address
    full_email = generate_email(full_index = full_index)

    # calculates date for graduation
    graduation_date = calculate_graduation_year(program = program_name,
                                                current_year = year_enrolled)  # Correct the variable name here

    # get relative program name
    str_program_name = get_object_or_404(Program, program_name = program_name)

    # Create a new instance for the current student
    new_student = Student.objects.create(
        email = full_email,
        index = full_index,
        program = str_program_name,
        year_enrolled = int(year_enrolled),  # Convert the current year to an integer
        # Other fields are set to default values, e.g., level, isInSchool, etc.
    )
    new_student.save()


def generate_email(full_index: str):
    """ Generating email address for student provided from full index number. 
    returns:
        str: full email address.
    """
    if full_index is not None:
        # Remove forward slashes from the index
        index = full_index.replace('/', '')

        # formatted string to create email
        address = f"{index}@ttu.edu.gh"

        return address
    return None


def generate_student_index(program: str, index: int, year: str, program_abbreviation: str, department: str):
    """
    Generate a student index based on the program type, index, year, program abbreviation, and department abbreviation.

    Returns:
        str: The generated student index as a string.
    """
    str_program = str(program)

    if str_program != 'hnd':
        # index for BTECH, DIPTECH, etc.
        formatted_index = f"{program_abbreviation}/{department}/{year[2:]}/{index:03}"
        return formatted_index

    else:
        # index for HND
        formatted_index = f"{program_abbreviation}{year[2:]}{index:06}"
        return formatted_index


def calculate_graduation_year(program: str, current_year: str):
    """
    Calculate the expected graduation year based on the program type and the current year.

    Args:
        program (str): The type of academic program (e.g., 'diptech', 'hnd', or other).
        current_year (str): The current year as a string.

    Returns:
        str: The calculated graduation year as a string.
    """
    # convert current year to integer to allow calculation
    this_year = int(current_year)

    graduation_years = {
        'diptech': this_year + 2,  # Graduation year for 'diptech' is current year + 2
        'hnd': this_year + 3,  # Graduation year for 'hnd' is current year + 3
    }

    # If the program type is not in the dictionary, default to adding 4 years to the current year
    return str(graduation_years.get(program, this_year + 4))
