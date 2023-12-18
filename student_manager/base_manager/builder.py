from base_manager.student_records import StudentRecord


class SingleStudentBuilder(StudentRecord):
    """
    Initialize a SingleStudentBuilder.
    """

    def __init__(self, index, course, program, year_enrolled=None):
        super().__init__(index)
        self.course = course
        self.program = program
        self.year_enrolled = year_enrolled


    def generate_index_number(self):
        """
        Generate the unique index number for the student.
        Returns:
        - str: The index number.
        """

        program_abbr = 'ict'

        if self.program != "hnd":
            return f"{program_abbr}{self.course}{self.year_enrolled[2:]}{int(self.index):03}"
        
        else:
            year_code = self.year_enrolled[2:]
            return f"{program_abbr}{year_code:05}{self.index:03}"

 


