from django.db import models
from user_registration.models import Doctor, Patient

# Create your models here.
class Reservation(models.Model):
   """
   Reservation to visit a doctor
   """
   doctor = models.ForeignKey(Doctor)
   patient = models.ForeignKey(Patient)
   datetime = models.DateTimeField()
