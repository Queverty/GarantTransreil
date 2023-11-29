from django import forms
from service_objects.fields import ModelField
from service_objects.services import Service

from transportation.models import PackingModel, CargoModel
from transportation.models.order.models import OrderModel
from user.models import User
from transportation.forms import PackingForm

class PackinContextDataServics(Service):
	user = ModelField(User)
	packing = forms.CharField()
	volume = forms.IntegerField()

	def process(self):
		self.order_save
		return {'packings': self.get_packing, 'order': self.get_order_user.last()}

	@property
	def order_save(self):
		orders = self.get_order_user
		order = orders.last()
		packing = self.get_packing.get(name=self.cleaned_data['packing'])
		order.packing = packing
		order.volume = self.cleaned_data['volume']
		order.save()
		return order

	@property
	def get_packing(self):
		return PackingModel.objects.all()

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])
