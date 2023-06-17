from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.getAllStudentDetails, name="allStudent"),
    path("student/create", views.createStudentDetails, name="createStudent"),
]

