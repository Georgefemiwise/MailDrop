"""
Module: runner.py

This module contains scheduling configurations for running tasks related to student management.

"""


from apscheduler.schedulers.background import BackgroundScheduler
from student_manager.schedules.auto_create_student import auto_create_student
from student_manager.schedules.update_student_count import get_highest_index

scheduler = BackgroundScheduler()

# Update student data every month (on the 1st day of each month)
scheduler.add_job(get_highest_index, "cron", month="1-4", day="1", hour="8")

# Run the auto-create student job once every year (on January 17th at 2 AM)
scheduler.add_job(auto_create_student, "cron", month="1", day="17", hour="2")

scheduler.start()
