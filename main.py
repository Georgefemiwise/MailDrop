import time
import json
from src.email.send_email import email_sender
from src.functions.constants import *
from src.functions.builder import SingleStudentBuilder

# TODO implement a better way to assign faculty to students
# def assign_faculty_and_department(program):
#     faculty = {'btech': 'bc'}
#     return faculty


def generate_student_data(course, program, num_students=200):
    """
    Generate data for multiple students from a given course and program,
    assuming that the students are in the same class.

    Parameters:
    - course (str): The course in which the students are enrolled.
    - program (str): The academic program of the students.
    - num_students (int, optional): The number of students to generate data for. Default is 200.

    The function creates student data based on the provided course and program,
    generating unique details such as index numbers, academic years, email addresses,
    graduation years, and school enrollment status. The data is stored in a JSON file.

    Example:
    generate_student_data(course="Computer Science", program="diptech", num_students=20)
    """

    students_data = []
    print("Processing...")

    for counter in range(1, num_students + 1):
        student = SingleStudentBuilder(
            year_enrolled=str(int(time.strftime("%Y")) - 2),
            index=str(counter),
            course=course,
            program=program,
        )

        students_data.append(
            {
                "index": student.generate_index_number(),
                "academic_year": f"{student.year_enrolled}/{int(student.year_enrolled) + 1}",
                "program": student.program,
                "email": student.generate_email(),
                "graduation": student.graduation_year(),
                "isInSchool": True,
            }
        )

    with open(FILENAME, "w") as f:
        json.dump(students_data, f, indent=4)

    print("Process completed successfully!")


if __name__ == "__main__":
    program = "btech"
    # program = "hnd"
    # program = 'diptech'

    course = "ict"

    # Start genearion
    generate_student_data(course=course, program=program)

    print("Sending emails...")
    # just to be certain let the program create the student first then sun it
    time.sleep(2)

    #
    email_sender()
