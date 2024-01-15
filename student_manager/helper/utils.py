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
    """Calculate the expected graduation year for the student"""

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
    Validates email address existence and returns True if it exists, defaulting to False if not.

    Args:
    - index (str): The index part of the email address.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    base_url = "https://api.ValidEmail.net/"
    email_domain = "ttu.edu.gh"
    email = f"{index}@{email_domain}"

    try:
        # Specify the parameters
        params = {
            "email": email,
            "token": "393475785da24fc684234580f893c9f4",  # Add your API token here
        }

        # Make the GET request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad response status codes

        # Handle the response
        data = response.json()
        is_valid = data.get("IsValid", False)
        return is_valid

    except requests.RequestException as e:
        # Log the error or handle it as needed
        print(f"Request failed with error: {e}")
        return False

    except Exception as e:
        # Log the unexpected error
        print(f"Unexpected error: {e}")
        return False
