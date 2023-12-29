import requests


def get_key_by_value(dictionary: dict, target_value: str):
    """
    Get the key associated with a specific value in a dictionary.

    Returns:
    - The key associated with the target value, or None if not found.
    """

    for key, value in dictionary.items():
        value = value.lower()
        target_value = target_value.lower()
        
        if value == target_value:
            return key
    return None


def generate_email(program, index, year, course):
    """
    Generate the unique index number for the student's email.

    Args:
        program (str): The program code, e.g., "bc" or "pd".
        index: The student's index number.
        year: The year of enrollment.
        course: The course abbreviation.

    Returns:
        str: The generated unique email for the student.
    """
    # Convert program code to lowercase for consistency
    program = f"{program}".lower()
    domain = "@ttu.edu.gh"

    if program in ("bc", "pd"):
        # For "bc" or "pd" programs
        generated_email = f"{program}{course}{year[2:]}{int(index):03}{domain}"
        return generated_email
    else:
        # For HND programs
        year_code = year[2:]
        generated_email = f"{program}{year_code:05}{index:03}{domain}"
        return generated_email


def cal_graduation_date(program, year):
    """
    Calculate the expected graduation year for the student.
    Returns:
    - str: The graduation year. Default 4 years.
    """

    if program == "diptech":
        # usally a 2 year course
        return str(2 + int(year))

    elif program == "hnd":
        # 3 year course
        return str(3 + int(year))

    else:
        # default to 4 years
        return str(4 + int(year))


def generate_index_number(program, index, year_enrolled, course):
    """
    Generate the unique index number for the student.
    Returns:
    - str: The index number.
    """

    if program != "hnd":
        return f"{program}{course}{year_enrolled[2:]}{int(index):03}".lower()

    else:
        year_code = year_enrolled[2:]
        return f"{program}{year_code:05}{index:03}"


def is_email_address_exists(index: str) -> bool:
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


# 0721000200
