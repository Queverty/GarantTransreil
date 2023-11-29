from django.db import models

from transportation.models import BaseModel


class CargoCategoriesModel(BaseModel):
	name = models.CharField(max_length=128, unique=True)
	img = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория груза"
		verbose_name_plural = "Категории грузов"
