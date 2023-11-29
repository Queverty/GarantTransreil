from transportation.models import BaseModel
from django.db import models


class WagonModel(BaseModel):
	type_wagon = models.CharField(max_length=256, unique=True)
	slug = models.SlugField(max_length=256, unique=True, db_index=True)
	img = models.ImageField()

	def __str__(self):
		return self.type_wagon

	class Meta:
		verbose_name = "Вагон"
		verbose_name_plural = "Вагоны"
