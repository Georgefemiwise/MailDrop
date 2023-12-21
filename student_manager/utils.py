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


def generate_email(program:str, index, year, course):
    """
    Generate the unique index number for the student.
    """
    program =program.lower()

    program_abbr = program
    

    if( program == "bc"):
        generated_email = f"{program_abbr}{course}{year[2:]}{int(index):03}"
        print(generated_email)
        return generate_email

    else:
        year_code = year[2:]
        generated_email = f"{program_abbr}{year_code:05}{index:03}"
        return generated_email


