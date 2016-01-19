from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_Details(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	"""
	User type:
		Buyer: 0
		Seller: 1
	"""
	u_type = models.PositiveSmallIntegerField(default=0)
	sex = models.CharField(max_length=10, blank=True)
	address = models.TextField(default="no address")
	contact = models.BigIntegerField(default=1234567890)
	image = models.CharField(max_length=50, default="default.png")
	def __str__(self):
		return self.user.username