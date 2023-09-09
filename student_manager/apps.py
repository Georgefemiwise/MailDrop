from django.apps import AppConfig


class StudentManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_manager'
    
    def ready(self):
        print("starting scheduler")
        from . auto import student_creater

        # start the process from the beginning of running the server
        student_creater.start()
        
