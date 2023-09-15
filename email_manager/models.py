from django.db import models
from ..student_manager.models import Student

class Message(models.Model):
    
    message = models.TextField(max_length=1000)
    to = models.ForeignKey(Student.email, on_delete=models.CASCADE)
    sender = models.ForeignKey()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message
  
