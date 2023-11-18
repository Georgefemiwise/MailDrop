import json
from src.functions.constants import FILENAME, CURRENT_YEAR


def update_is_in_school():
    """Update the is_in_school attribute of the student"""
    # Read the data from the JSON file
    with open(FILENAME, "r") as file:
        data = json.load(file)

    # Loop through the data and update isInSchool based on the comparison
    for item in data:
        if item["student"]["graduation"] <= CURRENT_YEAR:
            item["isInSchool"] = False
            print(item["index"], "no longer in school")

    # Save the updated data back to the JSON file
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
