# Student Updater and Creator Scheduler

This folder contains scripts for automating the update and creation of student records. The processes are scheduled to run periodically using a scheduler, such as cron in Unix-like systems.

## Overview
- **Annual Update**: The script for bi-monthly student creation runs twice every month, automating the process of generating new student records based on predefined criteria.


- **Bi-Monthly Creation**: The script for annual updates runs once every year to perform tasks such as updating graduation years and checking for changes in academic programs.


<!-- ## Usage

To set up the scheduler for these tasks, consider using a cron job or an equivalent scheduler on your system. Adjust the schedule to match the specific requirements of your organization or educational institution.

### Example (Cron Syntax)

```bash
# Annual Update (Run once a year, e.g., on January 1st)
0 0 1 1 * /path/to/annual_update_script.sh

# Bi-Monthly Creation (Run on the 1st and 15th of every month)
0 0 1,15 * * /path/to/bi_monthly_creation_script.sh


``` -->
