import time

from StudentRecorder import StudentRecord
from constants import PROGRAM_DICTIONARY


class SingleStudentBuilder(StudentRecord):
    """
    Represents a builder class for creating individual student records.

    Attributes:
    - year_enrolled (str): The year in which the student is enrolled.
    - program (str): The academic program in which the student is enrolled.
    - course (str): The specific course or specialization of the student.

    Methods:
    - generate_email(): Generates an email address for the student based on the program, course, and index.
    - graduation_year(): Calculates the expected graduation year for the student.
    - generate_index_number(): Generates the unique index number for the student.
    - raw_index_number(): Generates the raw index number for the student.
    """

    def __init__(self, index, course, program, year_enrolled=None):
        """
        Initialize a SingleStudentBuilder.

        Parameters:
        - index (str): The unique index number assigned to the student.
        - course (str): The specific course or specialization of the student.
        - program (str): The academic program in which the student is enrolled.
        - year_enrolled (str, optional): The year in which the student is enrolled. Default is None.
        """

        super().__init__(index)
        self.year_enrolled = year_enrolled or time.strftime("%Y")
        self.program = program
        self.course = course

    def generate_email(self):
        """
        Generate an email address for the student based on the program, course, and index.
        """

        program_abbr = PROGRAM_DICTIONARY[self.program]
        course_code = "ict" if self.program != "hnd" else "000"
        extension = f"{self.index:03}@ttu.edu.gh"

        if self.program == "hnd":
            return f"{program_abbr}{self.year_enrolled[2:]}{course_code}{extension}"
        else:
            return f"{program_abbr}{course_code}{self.year_enrolled[2:]}{extension}"

    def graduation_year(self):
        """
        Calculate the expected graduation year for the student.
        Returns:
        - str: The graduation year.
        """

        int_date = int(self.year_enrolled)

        if self.program == "diptech":
            return str(2 + int_date)
        elif self.program == "hnd":
            return str(3 + int_date)
        else:
            return str(4 + int_date)

    def generate_index_number(self):
        """
        Generate the unique index number for the student.
        Returns:
        - str: The index number.
        """

        program_abbr = PROGRAM_DICTIONARY[self.program]

        if self.program != "hnd":
            return f"{program_abbr}{self.course}{self.year_enrolled[2:]}{int(self.index):03}"
        else:
            year_code = self.year_enrolled[2:]
            return f"{program_abbr}{year_code:05}{self.index:03}"

    def raw_index_number(self):
        """
        Generate the raw index number for the student.
        Returns:
        - str: The raw index number.
        """

        return f"{self.index:03}"
