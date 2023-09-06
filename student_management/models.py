from datetime import datetime
from django.db import models


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=30, blank=True)
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)


class Department(models.Model):
    department_name = models.CharField( max_length=30, default="ict")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default='', null=True)
    
    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    
    def __str__(self):
        return f"{self.department_name[0].upper()+self.department_name[1:]} Department "


class Program(models.Model):
    program_name = models.CharField(max_length=30, default='')
    program_abbreviation = models.CharField(max_length=10, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')

    updated_at = models.DateTimeField(verbose_name='updated_at', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"

    def __str__(self):
        return self.program_name









class Student(models.Model):
    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        
        
    name = models.CharField(max_length=50, blank=True, default='')
    
    index = models.CharField(max_length=30, blank=True)
    email = models.CharField( max_length=60, unique=True, blank=True)
    isInSchool = models.BooleanField( default=True)
    year_enrolled = models.IntegerField( default=datetime.now().year)
    
    level = models.IntegerField( default=100)
    program = models.ForeignKey(Program,  on_delete=models.CASCADE,null=True)
        
    
    updated_at = models.DateTimeField( auto_now=True)
    created_at = models.DateTimeField( auto_now_add=True)


    def __str__(self):
        return self.index

