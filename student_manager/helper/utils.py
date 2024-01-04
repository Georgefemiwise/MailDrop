import requests

from student_manager.constants import PROGRAMS


def get_key_by_value(target_value: str):
    """
    Get the key associated with a specific value in a dictionary.

    Returns:
    - The key associated with the target value, or None if not found.
    """

    for key, value in PROGRAMS.items():
        value = value.lower()
        target_value = target_value.lower()

        if value == target_value:
            return key
    return None


def generate_email(index):
    """Generate the unique index number for the student's email from index."""

    return index + "@ttu.edu.gh"


def cal_graduation_date(program, year):
    """
    Calculate the expected graduation year for the student
    """
    program_durations = {"diptech": 2, "hnd": 3}

    program = program.lower()

    # If program is in the dictionary,
    # use its duration, otherwise default to 4 years
    duration = program_durations.get(program, 4)

    return str(duration + int(year))


def generate_index_number(program, index, _year_enrolled, course=None):
    """
    Generate the unique index number for the student.
    """
    index, _year_enrolled = str(index), str(_year_enrolled)

    if program == "07":
        return f"{program}{_year_enrolled:05}{index:03}"

    else:
        return f"{program}{course}{_year_enrolled[2:]}{int(index):03}".lower()


def is_valid_email_address(index: str) -> bool:
    """
    Validates email address existence and return True if it exists.
    default to False if not.

    https://docs.abstractapi.com/email-validation
    """
    try:
        url = "https://emailvalidation.abstractapi.com/v1/?api_key=c965ef8f1ac945f1bd0e0b0372a4e2c6&email="
        response = requests.get(f"{url}{index}@ttu.edu.gh")

        if response.status_code == 200:
            return True

        return False
    except Exception as e:
        print(e)
