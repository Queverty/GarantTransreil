from django.http import HttpResponse
from service_objects.fields import ModelField
from service_objects.services import Service

from transportation.models.order.models import OrderModel
from user.models import User


class OrderEndService(Service):
	user = ModelField(User)

	def process(self):
		user_info = self.cleaned_data['user']
		user_balance = user_info.balance
		oreders = self.get_order_user
		order = oreders.last()
		if order.status == 0 and order.price < user_balance:
			user_balance -= order.price
			order.status = 1
			order.save()
			user_info.balance = user_balance
			user_info.save()
			return {'order': order}
		else:
			return HttpResponse('Пополнение баланса прошло успешно!')

	@property
	def get_order_user(self):
		return OrderModel.objects.filter(user=self.cleaned_data['user'])
