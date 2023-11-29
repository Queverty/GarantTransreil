from django import forms

from transportation.models import StationModel, CargoModel, PackingModel, WagonModel
from transportation.models.order.models import OrderModel


class StationsForm(forms.ModelForm):
	stations = StationModel.objects.all()
	stations_list = []
	for num, pack in enumerate(stations):
		CHOICES = (f'{pack}', f'{pack}')
		stations_list.append(CHOICES)

	first_station = forms.ChoiceField(widget=forms.Select(attrs={
		'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}),choices=stations_list)
	second_station = forms.ChoiceField(widget=forms.Select(attrs={
		'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}),choices=stations_list)

	class Meta:
		model = StationModel
		fields = ('first_station', 'second_station',)

	def clean(self):
		if self.cleaned_data.get('first_station') == self.cleaned_data.get('second_station'):
			raise forms.ValidationError('Выберите разные станции!')
		return self.cleaned_data


class PackingForm(forms.ModelForm):
	packing = PackingModel.objects.all()

	pack_list = []
	for num, pack in enumerate(packing):
		CHOICES = (f'{pack}', f'{pack}')
		pack_list.append(CHOICES)

	name = forms.ChoiceField(widget=forms.Select(attrs={
		'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}), choices=pack_list)

	class Meta:
		model = PackingModel
		fields = ('name',)


class OrderForm(forms.ModelForm):
	volume = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number',
															  'class': 'form-control border-0 p-4',
															  'placeholder': 'Укажите вес, кг', }))

	class Meta:
		model = OrderModel
		fields = ('volume',)
