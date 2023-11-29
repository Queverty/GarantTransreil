from transportation.models import BaseModel, StationModel, CargoModel, PackingModel, WagonModel
from django.db import models

from user.models import User


class OrderModel(BaseModel):
	CREATED = 0
	PAID = 1
	ON_WAY = 2
	DELIVERED = 3
	STATUSES = (
		(CREATED, "Создан"),
		(PAID, "Оплачен"),
		(ON_WAY, "В пути"),
		(DELIVERED, "Доставлен"),
	)
	first_station = models.ForeignKey(to=StationModel, on_delete=models.CASCADE, related_name='station_from')
	second_station = models.ForeignKey(to=StationModel, on_delete=models.CASCADE, related_name='station_to', blank=True,
									   null=True)
	cargo = models.ForeignKey(to=CargoModel, on_delete=models.CASCADE, blank=True, null=True)
	packing = models.ForeignKey(to=PackingModel, on_delete=models.CASCADE, blank=True, null=True)
	wagon = models.ForeignKey(to=WagonModel, on_delete=models.CASCADE, blank=True, null=True)
	user = models.ForeignKey(to=User, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	dist = models.PositiveIntegerField(default=250)
	volume = models.PositiveIntegerField(blank=True, null=True)
	day = models.PositiveIntegerField(blank=True, null=True)
	creat = models.BooleanField(default=False)
	status = models.PositiveSmallIntegerField(default=CREATED, choices=STATUSES)

	def __str__(self):
		return f'Первозка от {self.first_station} до {self.second_station}'

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"
