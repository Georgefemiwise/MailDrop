enrol = 2021
grad = 2025
this_year = 2024
level = 100

# Calculate the number of years the student has been in school
if (this_year - enrol) >= 1:
    level = (this_year - enrol) * 100  # Increase the level by the number of years in school


# Adjust this as necessary
if level > (400):
    level = 400

print("Updated Level:", level)

