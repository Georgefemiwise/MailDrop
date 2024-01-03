# major school programs
import datetime


PROGRAMS: dict = {"BTECH": "BC", "DIPTECH": "PD", "HND": "07"}
COURSES: dict = {"computer science": "ict"}


CURRENT_YEAR: datetime = datetime.datetime.now().year
YEARS: tuple = (
    (CURRENT_YEAR - 0),
    (CURRENT_YEAR - 1),
    (CURRENT_YEAR - 2),
    (CURRENT_YEAR - 3),
)
