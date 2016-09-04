from django.db import models
from user_registration.models import Doctor, Patient

class Progress(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    content = models.CharField(max_length=500)
    datetime = models.DateTimeField()
