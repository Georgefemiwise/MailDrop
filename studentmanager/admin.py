from django.contrib import admin
from .models import *



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['name','updated_at','created_at',]
	


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display=['name','email', 'index', 'level', 'year_enrolled', 'program','updated_at', 'created_at', ]
 

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
	list_display=['name', 'department', 'updated_at', 'created_at',]



