from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from transportation.models import WagonModel
from transportation.models.order.models import OrderModel
from user.models import User


class WagonContextDataService(Service):
	user = ModelField(User)


	def process(self):
		return {'wagons': self.get_wagon, 'order': self.get_order_user.last()}


	@property
	def get_wagon(self):
		return WagonModel.objects.all()

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])
