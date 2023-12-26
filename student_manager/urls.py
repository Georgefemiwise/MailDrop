from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.all_students, name="all_students"),
    path("students/create/<str:index>/", views.create_student, name="create_student"),
    path(
        "students/course/<str:course>/",
        views.count_students_in_course,
        name="count_students_in_course",
    ),
    path(
        "students/year/<str:year_enrolled>/",
        views.count_students_in_year,
        name="count_students_in_year",
    ),
    path(
        "students/program/<str:program>/",
        views.count_students_in_program,
        name="count_students_in_program",
    ),
    path(
        "students/graduation/<str:graduation_year>/",
        views.count_students_graduating_in_year,
        name="count_students_graduating_in_year",
    ),
    path(
        "students/<str:index>/", views.get_student_by_index, name="get_student_by_index"
    ),
    # Add more paths as needed
]
