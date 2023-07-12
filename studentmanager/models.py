from datetime import datetime
from django.db import models


class Department(models.Model):
    name = models.CharField(verbose_name="department name", max_length=30, default="computer science ")
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    
    def __str__(self):
        return f"{self.name[0].upper()+self.name[1:]} Department "


class Program(models.Model):
    DIPLOMA = "DIP"
    HIGHER_NATIONAL_DIPLOMAS = "HND"
    BACHELOR_OF_TECHNOLOGY = "BTECH"
    PROGRAMS = [
        (DIPLOMA, 'Diploma'),
        (HIGHER_NATIONAL_DIPLOMAS, 'Higher National Diplomas'),
        (BACHELOR_OF_TECHNOLOGY, 'Bachelor of Technology'),
    ]



    name = models.CharField(choices=PROGRAMS, max_length=10, default=BACHELOR_OF_TECHNOLOGY)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, default='student')
    index = models.IntegerField(verbose_name='Student index number', blank=True)
    email = models.CharField(verbose_name='Email address', max_length=60, unique=True, blank=True)
    level = models.IntegerField(verbose_name='Level of study', default=100)
    year_enrolled = models.IntegerField(verbose_name='Year enrolled', default=datetime.now().year)
    program = models.ForeignKey(Program, verbose_name="Program of study", on_delete=models.CASCADE,null=True)

    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return self.email

