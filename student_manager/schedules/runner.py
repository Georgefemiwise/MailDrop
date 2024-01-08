"""handles the the scripts to be scheduled"""


from apscheduler.schedulers.background import BackgroundScheduler
from student_manager.schedules.auto_create_student import auto_create_student
from student_manager.schedules.update_student_count import get_highest_index


scheduler = BackgroundScheduler()


# update student data every month
scheduler.add_job(get_highest_index, "cron", month="1-12", day="*/15")

# run the scheduler once every year
scheduler.add_job(auto_create_student, "cron", month="2", day="15")

scheduler.start()
