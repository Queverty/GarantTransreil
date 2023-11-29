from transportation.models import BaseModel
from django.db import models
from transportation.models.cargocategories.models import CargoCategoriesModel

class CargoModel(BaseModel):
	name = models.CharField(max_length=256, unique=True)
	code = models.PositiveIntegerField()
	type_cargo = models.ForeignKey(to=CargoCategoriesModel,on_delete=models.CASCADE)
	price = models.PositiveIntegerField()
	slug = models.SlugField(max_length=256, unique=True, db_index=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Груз"
		verbose_name_plural = "Грузы"