from transportation.models import BaseModel
from django.db import models


class PackingModel(BaseModel):
	name = models.CharField(max_length=256, unique=True)
	slug = models.SlugField(max_length=256, unique=True, db_index=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Упаковка"
		verbose_name_plural = "Упаковки"