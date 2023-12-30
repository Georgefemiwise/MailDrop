# student_manager/models.py

from django.db import models


class Student(models.Model):
    index = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=20, blank=True, default='Unknown Course')
    program = models.CharField(max_length=10, null=False)
    year_enrolled = models.CharField(max_length=4)
    graduation_year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.index} - {self.course} - {self.program}"
