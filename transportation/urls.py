from django.urls import path

from transportation.views import InedexView, StationsSelectedView, CargoSelectedView, PackingSelectedView, \
	WagonSelectedView, DayListView, DaySelectView, OrderView

urlpatterns = [
	path('', InedexView.as_view(), name='index'),
	path('order-create/', StationsSelectedView.as_view(), name='order-create'),
	path('order-creat/<slug:slug1>-<slug:slug2>/', CargoSelectedView.as_view(), name='cargos'),
	path('order-creat/<slug:slug1>-<slug:slug2>/<slug:slug3>/', PackingSelectedView.as_view(), name='packing'),
	path('order-creat/<slug:slug1>-<slug:slug2>/<slug:slug3>/<slug:slug4>/', WagonSelectedView.as_view(),
		 name='wagons'),
	path('order-creat/<slug:slug1>-<slug:slug2>/<slug:slug3>/<slug:slug4>/<slug:slug5>/', DayListView.as_view(),
		 name='day'),
	path('order-creat/<slug:slug1>-<slug:slug2>/<slug:slug3>/<slug:slug4>/<slug:slug5>/day-<int:day>/',
		 DaySelectView.as_view(), name='order-end'),
	path('order-accept/<slug:slug1>-<slug:slug2>/<slug:slug3>/<slug:slug4>/<slug:slug5>/day-<int:day>/',
		 OrderView.as_view(), name='order'),
]
