# Maildrop
Django Student Management System



## Overview

This Django project serves as a Student Management System designed to create and manage student details. Each student record includes essential information such as the student's ID, index, email address, course, program, year of enrollment, and expected graduation year. Additionally, the system periodically verifies and updates student email addresses during specific months to ensure deliverability.

## Student Record Format

Each student record adheres to the following format:

```json
{
    "id": 1,
    "index": "bcict21001",
    "email": "bcict21001@ttu.edu.gh",
    "course": "ict",
    "program": "BTECH",
    "year_enrolled": "2021",
    "graduation_year": "2025"
}
```

## Email Verification Process

The system incorporates an annual email verification process that occurs during specified months. This process aims to validate the deliverability of student email addresses. If an email address is identified as undeliverable, the system takes appropriate actions to update or correct the email information.

<!-- ## Project Structure

The project is structured as follows:

- **`src/`:** Contains the Django application source code.
- **`data/`:** Houses data files, including student records.
- **`scripts/`:** Includes scripts related to the project, such as email verification scripts. -->

## Getting Started

To run the Django project locally:

1. Set up a virtual environment: `python -m venv venv` and activate it.
2. Install project dependencies: `pip install -r requirements.txt`.
3. Apply migrations: `python manage.py migrate`.
4. Run the Django development server: `python manage.py runserver`.

Navigate to `http://127.0.0.1:8000/` to access the Django admin interface and manage student records.

## Usage

Explore and interact with the Django admin interface to add, update, and manage student details. Adjust the project as needed for your specific requirements.

If you have any questions or encounter issues, refer to the documentation or reach out to the project maintainers.

Feel free to enhance and customize the project to suit your needs. Happy coding!