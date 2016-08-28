from django.db import models
from django.contrib.auth.models import User

class Progress(models.Model):
    doctor = models.ForeignKey(User, to_field="username")
    patient = models.ForeignKey(User, to_field="username")
    content = models.CharField(max_length=500)
    dateTime = models.DateTimeField()
    
