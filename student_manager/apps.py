from django.apps import AppConfig


class StudentManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_manager'
    
    def ready(self):
        print("starting scheduler")
        from . base_creator import create_multiple_student

        # start the process from the beginning of running the server
        create_multiple_student.start_creation()
        
