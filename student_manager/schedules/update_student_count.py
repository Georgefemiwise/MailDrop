from ..constants import COURSES, PROGRAMS, YEARS
from ..models import Student


def try_increment_of_student(highest_index_student):
    """
    The function  increments the index of the highest indexed student by 10
    and creates new student objects with the incremented indices.
    
    :param highest_index_student: The parameter `highest_index_student` is expected to be an instance of
    the `Student` model class. It represents the student with the highest index value in the database
    """

    if highest_index_student is not None:
        # Extract the numeric part of the index and increment by 10
        current_index = int(highest_index_student.index[-3:])
        new_index = current_index + 10

        # Create and save new students with incremented indices
        for index in range(current_index, new_index):
            Student.objects.create(
                index=index,
                email=f"{index}@ttu.edu.gh",
                course=highest_index_student.course,
                program=highest_index_student.program,
                year_enrolled=highest_index_student.year_enrolled,
                graduation_year=highest_index_student.graduation_year,
            )
    else:
        # Handle the case where no student with an index is found
        pass


def get_highest_index():
    """
    The function retrieves the student with the highest index from a specific
    program, course, and year, and then increments the student's index.
    """

    
    highest_index_student = None
    max_index = None

    # todo this course check needs a better implementation for other courses
    # defalut is computer science
    course = COURSES["computer science"]

    for program_code in PROGRAMS.keys():
        for year in YEARS:
            # Retrieve the students for the given program, course, and year
            students = Student.objects.filter(
                year_enrolled=str(year),
                program=program_code,
                course=course,
            )

            # Check if there are any students
            if students.exists():
                # Find the student with the highest index in the current iteration
                current_max_index = students.order_by("-index").first().index

                # Check if the retrieved index is higher than the current max
                if max_index is None or current_max_index > max_index:
                    max_index = current_max_index
                    highest_index_student = students.filter(index=max_index).first()
                    try_increment_of_student(highest_index_student)
