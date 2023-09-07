
import time
from ..models import Student, Program,Department
from apscheduler.schedulers.background import BackgroundScheduler
import json


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(create_multiple_students, "interval", seconds=20)
    scheduler.start()


students_data = []



def create_multiple_students():
    # get programs from the database
    list_of_programs = Program.objects.all()
    
    range_of_students = 5
    
    print( "Creating multiple students")
  
    for program in list_of_programs:
        for index in range(range_of_students):
            create_single_student(program, index)
            
    save_student_data_to_json(students_data)
            
   
    
    
    
def create_single_student(program, index):
    CURRENT_YEAR = time.strftime('%Y')

    full_index = generate_student_index(program=program, index=index, year=CURRENT_YEAR)
    full_email = generate_email(Full_index=full_index)  # Correct the variable name here
    program_instance = Program.objects.get(program_name=program)
    graduation_date = calculate_graduation_year(program=program, current_year=CURRENT_YEAR)  # Correct the variable name here

    # Create a new instance for the current student
    # new_student = Student.objects.create(
    #     email=full_email,
    #     index=full_index,
    #     program=program_instance,
    #     year_enrolled=int(CURRENT_YEAR),  # Convert the current year to an integer
    #     # Other fields you want to set, e.g., level, isInSchool, etc.
    # )
    
    # # Print information about the created student
    studen_info = {
        'full_email': full_email,
        'program_name': program_instance.program_name,
        'full_index': full_index,
        'graduation_date': graduation_date,
    }
    students_data.append(studen_info)

        
def save_student_data_to_json(data):
    json_filename = 'students.json'

    # Write the list of student data to the JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    
    
def generate_email(Full_index):
    r"Generating email address from index number of students."
    
    index = Full_index.replace('/', '') # Remove forward slashes from the index
    address = f"{index}@ttu.edu.gh"
    return address

    

def generate_student_index(program: str, index: int, year: str):
    """
    Generate a student index based on the program type, index, and current year.

    Returns:
        str: The generated student index as a string.
    """
    # todo: should be able to take abriviation from db rather than hardcoded
    
    
    try:
        get_program =  Program.objects.get(program_name=program)
        
        program_abbreviation = get_program.program_abbreviation
        department = get_program.department.department_name
        
    except Program.DoesNotExist:
        return None
        
    
    if program != 'hnd':
        index_format = f"{program_abbreviation}/{department}/{year[2:]}/{index:03}"
    
    else:
        index_format = f"{program_abbreviation}{year[2:]}{index:06}"

    return index_format



def calculate_graduation_year(program: str, current_year: str):
    """
    Calculate the expected graduation year based on the program type and the current year.

    Args:
        program (str): The type of academic program (e.g., 'diptech', 'hnd', or other).
        current_year (str): The current year as a string.

    Returns:
        str: The calculated graduation year as a string.
    """
    
    
    this_year = int(current_year)
    
   
    graduation_years = {
        'diptech': this_year + 2,  # Graduation year for 'diptech' is current year + 2
        'hnd': this_year + 3,      # Graduation year for 'hnd' is current year + 3
    }
    
    # If the program type is not in the dictionary, default to adding 4 years to the current year
    return str(graduation_years.get(program, this_year + 4))

    


    
