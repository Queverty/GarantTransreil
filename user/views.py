import uuid
from http import HTTPStatus

import stripe
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView

from common.views import TitleMixin
from .models import User
from user.forms import UserProfileForm, UserRegisterForm, UserLoginForm, UserBalanceForm
from user.services.orders.list import OrderListServieces
from .services.balance.succless import BalanceUppdateService
from .services.orders.get_by_id import OrderIdServieces
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

class ProfileView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'user/profile.html', context={"title": "Личный кабинет"})


class ProfileEditView(TitleMixin, UpdateView):
	model = User
	form_class = UserProfileForm
	template_name = 'user/profile_edit.html'
	title = 'Изменить личные данные'

	def get_success_url(self):
		return reverse_lazy('user:profile', args=(self.object.id,))


class OrderListView(View):

	def get(self, request, *args, **kwargs):
		outcome = OrderListServieces.execute({'user': request.user})
		return render(request, 'user/orders.html', context={'orders': outcome, "title": "Ваши заказы"})


class OrderDetailView(View):

	def get(self, request, *args, **kwargs):
		outcome = OrderIdServieces.execute({'order_id': kwargs['order']})
		return render(request, 'user/order-detail.html',
					  context={'order': outcome, 'title': f"Ваш заказ № "})


class UserRegistrationView(TitleMixin, CreateView):
	model = User
	form_class = UserRegisterForm
	template_name = 'user/registration.html'
	success_url = reverse_lazy('index')
	title = "Регистрация"


class UserLoginView(TitleMixin, LoginView):
	form_class = UserLoginForm
	template_name = 'user/login.html'
	success_url = reverse_lazy('index')
	title = "Авторизация"


class UserBalanceView(View):

	def post(self, request, *args, **kwargs):
		stripe_product = stripe.Product.create(name="Balance")
		stripe_product_price = stripe.Price.create(
			product=stripe_product['id'], unit_amount=int(request.POST['balance']) * 100, currency='rub')
		checkout_session = stripe.checkout.Session.create(
			line_items=[{
				'price': stripe_product_price['id'],
				'quantity': 1,
			}],
			mode='payment',
			success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('user:balance-succless',
																	)),
			cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('index')),
			metadata={'user': request.user},
		)
		return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

	def get(self, request, *args, **kwargs):
		return render(request, 'user/balance_pay.html', context={'form': UserBalanceForm})


@csrf_exempt
def stripe_webhook_view(request):
	sig_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None
	payload = request.body
	try:
		event = stripe.Webhook.construct_event(
			payload, sig_header, settings.STRIPE_WEBHOOK
		)
	except ValueError:
		# Invalid payload
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError:
		# Invalid signature
		return HttpResponse(status=400)

	# Handle the checkout.session.completed event
	if event['type'] == 'checkout.session.completed':
		session = event['data']['object']

		# Fulfill the purchase...
		fulfill_order(session)

	# Passed signature verification
	return HttpResponse(status=200)


def fulfill_order(session):
	user = session['metadata']['user']
	amount_total = (session["amount_total"] // 100)
	outcome = BalanceUppdateService.execute({'user': user, 'balance': amount_total})


class SucclessBalanceView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'user/success_balance.html', context={"title": "Баланс пополнен"})
