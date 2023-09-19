from ..models import Student
from datetime import datetime


current_year = datetime.now().year


def _update_student_():
    pass


def update_graduation():
    pass


def update_is_in_school():
    pass


def update_specialization():
    pass


def update_level():
    r"""update level of students specifically from the program they offer."""

    # get all student
    students = Student.objects.all()

    for student in students:
    
        # increment student level
        new_level = student.level * (current_year - student.year_enrolled)

        if student.program == 'diptech':
            max_level = 200
        elif student.program == 'hnd':
            max_level = 300
        else:
            max_level = 400

        # maximum level check 
        if new_level > max_level:
            new_level = max_level

        student.level = new_level
        student.save()
