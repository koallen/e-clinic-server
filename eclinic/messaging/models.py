from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MessageToken(models.Model):
	token = models.CharField(max_length=200)
	username = models.ForeignKey(User)


