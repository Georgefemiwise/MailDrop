from django.db import models

class Messages(models.Model):
    email = models.EmailField( max_length=254)
