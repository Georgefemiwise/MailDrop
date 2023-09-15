enrol = 2021
grad = 2025
this_year = 2024
level = 100

# Calculate the number of years the student has been in school
years_in_school = this_year - enrol

# Adjust the level based on the years in school
if years_in_school >= 1:
    level = years_in_school * 100  # Increase the level by the number of years in school

# Make sure the level does not exceed a certain maximum level (if needed)
max_level = 400  # Adjust this as necessary
if level > max_level:
    level = max_level

print("Updated Level:", level)

