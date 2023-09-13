from datetime import datetime
from django.db import models


class Faculty(models.Model):
    faculty_name = models.CharField(max_length = 30, blank = True)
    updated_at = models.DateTimeField(verbose_name = 'updated_at', auto_now = True)
    created_at = models.DateTimeField(verbose_name = 'Created at', auto_now_add = True)

    class Meta:
        verbose_name_plural = "faculties"

    def __str__(self):
        return f"faculty of {self.faculty_name}"


class Program(models.Model):
    program_name = models.CharField(max_length = 30, default = '')
    program_abbreviation = models.CharField(max_length = 5, default = '')

    updated_at = models.DateTimeField(verbose_name = 'updated_at', auto_now = True)
    created_at = models.DateTimeField(verbose_name = 'Created at', auto_now_add = True)

    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"

    def __str__(self):
        return self.program_name


class Department(models.Model):
    department_name = models.CharField(max_length = 30, default = "ict")
    department_abbreviation = models.CharField(max_length = 5, default = "")
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE, default = '', )

    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.department_name[0].upper() + self.department_name[1:]} Department"


class Student(models.Model):
    name = models.CharField(max_length = 50, blank = True, default = '')
    index = models.CharField(max_length = 15, blank = True)

    email = models.CharField(max_length = 23, blank = True)
    isInSchool = models.BooleanField(default = True)

    year_enrolled = models.IntegerField(default = 2023)
    graduation_date = models.IntegerField(default = 0000)

    level = models.IntegerField(default = 100)
    program = models.ForeignKey(Program, on_delete = models.CASCADE, null = True)

    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True, )

    def __str__(self):
        return self.index
