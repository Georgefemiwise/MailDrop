class StudentRecord:
    """
    Represents a base class for student records.

    Attributes:
    - name (str): The name of the student.
    - index (str): The unique index number assigned to the student.
    - program (str): The academic program in which the student is enrolled.
    - course (str): The specific course or specialization of the student.
    - level (str): The academic level or year of the student.
    - graduation (str): The expected year of graduation for the student.
    - enrolled (str): The enrollment year of the student.
    """

    def __init__(self, index):
        self.name = None
        self.index = index
        self.program = None
        self.course = None
        self.level = None
        self.graduation = None
        self.enrolled = None
