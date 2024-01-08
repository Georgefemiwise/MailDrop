from django.apps import AppConfig


class StudentManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_manager'

    def ready(self):
        
        from .schedules import runner
        runner

