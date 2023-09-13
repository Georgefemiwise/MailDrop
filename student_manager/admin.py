from django.contrib import admin
from .models import *


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_name', 'updated_at', 'created_at', ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'department_abbreviation', 'updated_at', 'created_at', ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'index', 'level', 'year_enrolled', 'program', 'updated_at', 'created_at', ]
    list_filter = ['email', 'index', 'level']
    list_per_page = 200


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program_name', 'program_abbreviation', 'updated_at', 'created_at', ]
