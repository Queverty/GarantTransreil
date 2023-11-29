from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from transportation.models import CargoModel
from transportation.models.order.models import OrderModel
from user.models import User


class CargoContextDataService(Service):
	user = ModelField(User)

	def process(self):
		return {'cargos': self.get_cargos, 'order': self.get_order_user.last()}

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])

	@property
	def get_cargos(self):
		return CargoModel.objects.all()

