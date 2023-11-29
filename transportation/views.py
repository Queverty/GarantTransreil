from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from common.views import TitleMixin
from transportation.forms import StationsForm, PackingForm, OrderForm
from transportation.services.cargo.context_data import CargoContextDataService
from transportation.services.day.list import DayListService
from transportation.services.day.save import DataSaveService
from transportation.services.order.end import OrderEndService
from transportation.services.order.get import OrderGetService
from transportation.services.order.station_selected import StationSelectedService
from transportation.services.packing.context_data import PackinContextDataServics
from transportation.services.packing.list import PackingListService
from transportation.services.stations.context_data import StationsContextDataService
from transportation.services.wagon.context_data import WagonContextDataService


# Create your views here.


class InedexView(TitleMixin, TemplateView):
	template_name = "transportation/index.html"
	title = 'ГарантТраснрейл'


class StationsSelectedView(View):

	def post(self, request):
		form = StationsForm(request.POST)
		if form.is_valid():
			outcome = StationSelectedService.execute(
				{'user': request.user,
				 'first_station': request.POST['first_station'],
				 'second_station': request.POST['second_station'], })
			return HttpResponseRedirect(
				reverse('cargos', kwargs={'slug1': outcome.first_station.slug,
										  'slug2': outcome.second_station.slug}))

	def get(self, request, *args, **kwargs):
		stations = StationsContextDataService.execute({})
		context = {'stations': stations['stations'], 'form': StationsForm, 'title': 'Новая перевозка'}
		return render(request, template_name="transportation/stations.html", context=context)


class CargoSelectedView(View):

	def get(self, request, *args, **kwargs):
		outcome = CargoContextDataService.execute({'user': request.user, })
		return render(request, template_name="transportation/cargo.html",
					  context={'cargos': outcome['cargos'], 'order': outcome['order'],
							   'title': 'Выбор груза для отправки'})


class PackingSelectedView(View):

	def get(self, request, *args, **kwargs):
		outcome = PackingListService.execute({'user': request.user, 'cargo': kwargs['slug3'], })
		return render(request, template_name='transportation/packing.html',
					  context={'form2': PackingForm,
							   'form3': OrderForm,
							   'order': outcome['order'],
							   'packing': outcome['packing'],
							   'title': 'Выбор упаковки и веса', })

	def post(self, request, *args, **kwargs):
		outcome = PackinContextDataServics.execute(
			{'user': request.user,
			 'packing': request.POST['name'],
			 'volume': request.POST['volume'], })
		return HttpResponseRedirect(reverse('wagons', kwargs={'slug1': outcome['order'].first_station.slug,
															  'slug2': outcome['order'].second_station.slug,
															  'slug3': outcome['order'].cargo.slug,
															  'slug4': outcome['order'].packing.slug, }))


class WagonSelectedView(View):
	def get(self, request, *args, **kwargs):
		outcome = WagonContextDataService.execute({'user': request.user})
		return render(request, template_name='transportation/wagon.html',
					  context={'wagons': outcome['wagons'], 'order': outcome['order'], 'title': "Выбор типа вагона"})


class DayListView(View):
	def get(self, request, *args, **kwargs):
		outcome = DayListService.execute({'user': request.user, 'slug': kwargs['slug5']})
		return render(request, template_name='transportation/day.html',
					  context={'data': outcome['data'], 'month': outcome['month'], 'order': outcome['order'],
							   'title': "Выбор даты доставки"})


class DaySelectView(View):
	def get(self, request, *args, **kwargs):
		if kwargs['day']:
			outcome = DataSaveService.execute({'user': request.user, 'day': kwargs['day']})
		else:
			outcome = OrderGetService.execute({'user': request.user})
		return render(request, template_name='transportation/ordercreate.html',
					  context={'order': outcome, 'title': "Оформление заказа"})


class OrderView(View):

	def get(self, request, *args, **kwargs):
		outcome = OrderEndService.execute({'user': request.user})
		return render(request, template_name='transportation/order.html',
					  context={'order': outcome['order'], "title": "Зазказ оформлен"})
