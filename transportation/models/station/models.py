from django.urls import reverse

from transportation.models import BaseModel
from django.db import models


class StationModel(BaseModel):
	name = models.CharField(max_length=256, unique=True)
	slug = models.SlugField(max_length=256, unique=True, db_index=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Станция"
		verbose_name_plural = "Станции"


	def get_second_slug(self):
		return reverse('second_station',kwargs={'second_slug':self.slug})