from datetime  import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    index = models.IntegerField(verbose_name='Student index number')
    program = models.CharField(verbose_name='Program of study', max_length=30)
    email = models.CharField(verbose_name='Email address', max_length=60)
    level = models.IntegerField(verbose_name='Level of study', default=100)
    year_enrolled = models.IntegerField(verbose_name='Year enrolled', default=datetime.now().year)

    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now, auto_now=False, auto_now_add=False)
     
    def __str__(self):
        return self.email



