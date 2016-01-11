from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_Details(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sex = models.CharField(max_length=10)
	address = models.TextField(default="no address")
	contact = models.BigIntegerField(default=1234567890)
	image = models.CharField(max_length=50)