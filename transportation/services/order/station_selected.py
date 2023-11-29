from service_objects.fields import ModelField
from service_objects.services import Service

from transportation.models import StationModel
from transportation.models.order.models import OrderModel
from user.models import User
from django import forms


class StationSelectedService(Service):
	user = ModelField(User)
	first_station = forms.CharField()
	second_station = forms.CharField()


	def process(self):
		first_station = self.get_stantions.get(name=self.cleaned_data['first_station'])
		second_station = self.get_stantions.get(name=self.cleaned_data['second_station'])
		orders = self.get_order_user
		order = orders.create(user=self.cleaned_data['user'],first_station=first_station,second_station=second_station)
		return order

	@property
	def get_stantions(self):
		return StationModel.objects.all()

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])
