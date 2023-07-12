from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_all_students, name='get_all_students'),
    path('students/create/', views.create_student, name='create_student'),

    path('students/<int:student_index>/get/', views.get_student, name='get_student'),
    path('students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    
    path('departments/', views.get_all_departments, name='get_all_departments'),
    
    path('programs/', views.get_all_programs, name='get_all_programs'),
    
    # Todo: create a better way to get the list of programs through the url here
    # path('students/<int:program>', views.students_in_program, name='students_in_program'),
]
