from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from transportation.models import BaseModel


class User(AbstractUser,BaseModel):
	phone = PhoneNumberField(null=True, blank=True)
	img = models.ImageField(upload_to='users/%Y/%m/%d/', null=True, blank=True)
	is_verified_email = models.BooleanField(default=False)
	email = models.EmailField(unique=True, null=True, blank=True)
	balance = models.PositiveIntegerField(default=0,null=True, blank=True)

	def update_after_payment(self,amount):
		user_balance = self.balance
		user_balance += amount
		self.save()