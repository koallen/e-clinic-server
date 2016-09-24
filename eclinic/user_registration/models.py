from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    """
    Doctor information
    """
    user = models.OneToOneField(User, to_field="username", related_name="doctor")
    clinic = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    description = models.CharField(max_length=500)

    def get_username(self):
        return self.user.username

class Patient(models.Model):
    """
    Patient information
    """
    user = models.OneToOneField(User, to_field="username", related_name="patient")
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

    def get_username(self):
        return self.user.username
