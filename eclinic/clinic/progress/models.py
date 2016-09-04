from django.db import models
from user_registration.models import Doctor, Patient

class Progress(models.Model):
    doctor = models.ForeignKey(Doctor, to_field="user")
    patient = models.ForeignKey(Patient, to_field="user")
    content = models.CharField(max_length=500)
    dateTime = models.DateTimeField()
