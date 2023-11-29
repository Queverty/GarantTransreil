from django.contrib import admin

from transportation.models import StationModel, CargoModel, CargoCategoriesModel, PackingModel, WagonModel
from transportation.models.order.models import OrderModel


# Register your models here.
@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
	list_display = (
	'first_station', 'second_station', 'cargo', 'packing', 'wagon', 'user', 'price', 'dist', 'volume', 'day', 'status')
	search_fields = ('user',)

class StationAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}


class CargoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}


@admin.register(PackingModel)
class PackingAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}


class WagonAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("type_wagon",)}


admin.site.register(StationModel, StationAdmin)
admin.site.register(CargoModel, CargoAdmin)
admin.site.register(CargoCategoriesModel)
admin.site.register(WagonModel, WagonAdmin)
