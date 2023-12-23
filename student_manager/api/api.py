import requests


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
