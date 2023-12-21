# student_manager/models.py

from django.db import models


class Student(models.Model):
    index = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    year_enrolled = models.IntegerField()

    # email = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.index} - {self.course} - {self.program}"
