import requests


def get_key_by_value(dictionary: dict, target_value: str):
    """
    Get the key associated with a specific value in a dictionary.

    Returns:
    - The key associated with the target value, or None if not found.
    """
    for key, value in dictionary.items():
        if value.lower() == target_value.lower():
            return key
    return None


def is_email_address_exists(index):
    """
    https://docs.abstractapi.com/email-validation
    """

    response = requests.get(
        f"https://emailvalidation.abstractapi.com/v1/?api_key=c965ef8f1ac945f1bd0e0b0372a4e2c6&email={index}@ttu.edu.gh"
    )

    if response.status_code == 200:
        # print(response.content)
        return True

    return False


def generate_email(program: str, index, year, course):
    """
    Generate the unique index number for the student's email.

    Args:
        program (str): The program code, e.g., "bc" or "pd".
        index: The student's index number.
        year: The year of enrollment.
        course: The course code.

    Returns:
        str: The generated unique email for the student.
    """
    # Convert program code to lowercase for consistency
    program = program.lower()

    if program in ("bc", "pd"):
        # For "bc" or "pd" programs
        generated_email = f"{program}{course}{year[2:]}{int(index):03}"
        return generated_email
    else:
        # For other programs
        year_code = year[2:]
        generated_email = f"{program}{year_code:05}{index:03}"
        return generated_email
