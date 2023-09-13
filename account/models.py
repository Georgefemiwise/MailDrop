from django.db import models

from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 255)
    industry = models.CharField(max_length = 50)
    relationship = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    created_at = models.DateTimeField(auto_now = True, )
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length = 20)
    whatsapp = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.phone
