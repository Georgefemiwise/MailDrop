from django.db import models
from django.utils import timezone

# Create your models here.

class BachelorsDegreeAddresses(models.Model):
     Address = models.CharField(max_length= 50)
     date = models.DateTimeField( default=timezone.now ,auto_now=False, auto_now_add=False)

     def __str__ (self) -> str:
          return self.Address


class test(models.Model):
     address = models.CharField(max_length= 50)
    
     def __str__ (self) -> str:
          return self.address