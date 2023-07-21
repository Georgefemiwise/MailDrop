from django.urls import path
from . import views

urlpatterns = [
    path('api/students/', views.get_all_students, name='get_all_students'),
   path('api/students/create/', views.create_student, name='new_student'),


    path('api/students/<int:student_index>/get/', views.get_student, name='get_student'),
    path('api/students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('api/students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    
    path('api/departments/', views.get_all_departments, name='get_all_departments'),
    
    path('api/programs/', views.get_all_programs, name='get_all_programs'),
    
    path('api/students/<int:programID>/', views.students_in_program, name='students_in_program'),

]
