from service_objects.fields import ModelField
from service_objects.services import Service

from transportation.models.order.models import OrderModel
from user.models import User


class OrderGetService(Service):
	user = ModelField(User)

	def process(self):
		oreder = self.get_order_user
		return oreder.last()

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])
