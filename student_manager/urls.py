from django.urls import path
from . import views

urlpatterns = [
    path("students/all/", views.all_student),
    path("students/create/last/<str:index>/", views.last_index),

   
]
