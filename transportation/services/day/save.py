from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service
from transportation.models.order.models import OrderModel
from user.models import User
from geopy.distance import geodesic as GD
from yandex_geocoder import Client
from decimal import Decimal
class DataSaveService(Service):
	user = ModelField(User)
	day = forms.IntegerField()

	def process(self):
		order = self.get_order_user.last()
		order.day = self.cleaned_data['day']
		price_per_kg = order.cargo.price
		price = (order.dist * (price_per_kg/10) * (order.volume/100))/10
		order.price = price
		order.save()
		# self.get_distations()
		return order

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])

	def get_distations(self):
		order = self.get_order_user.last()
		first_station = order.first_station
		second_station = order.second_station
		client = Client("56e81842-36ab-4123-9d54-179d9b881640")
		coordinates1 = client.coordinates(first_station)
		coordinates2 = client.coordinates(second_station)
		distations = GD(coordinates1, coordinates2).km
		order.dist = distations
		order.save()
		return order


	# def get_pirce(self):
	# 	order = self.get_order_user.last()
	# 	price = order.dist * 100 * (order.volume/10000)
	# 	order.price = Decimal(price)
	# 	order.save()
