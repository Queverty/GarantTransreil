from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from user.models import User


class UserProfileForm(UserChangeForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control border-0 p-3', 'style': 'height: 27px;'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control border-0 p-3', 'style': 'height: 27px;'}))
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control border-0 p-3', 'style': 'height: 27px;', 'readonly': True}))
	email = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control border-0 p-3', 'style': 'height: 27px;', 'readonly': True}))
	phone = forms.CharField(
		widget=forms.TextInput(attrs={'class': 'form-control border-0 p-3', 'style': 'height: 27px;'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'phone')

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'type': "text",
		'class': 'form-control border-0 p-3',
		'placeholder': "Введите логин"
	}))
	phone = forms.CharField(widget=forms.TextInput(attrs={
		'type': "text",
		'class': 'form-control border-0 p-3',
		'placeholder': "Введите номер телефона"
	}))
	email = forms.CharField(widget=forms.TextInput(attrs={
		'type': "text",
		'class': 'form-control border-0 p-3',
		'placeholder': "Введите email"
	}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={
		'type': "password",
		'class': 'form-control border-0 p-3',
		'placeholder': "Повторите пароль"
	}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={
		'type': "password",
		'class': 'form-control border-0 p-3',
		'placeholder': "Введите пароль"
	}))

	class Meta:
		model = User
		fields = ('username', 'phone', 'password1', 'password2', 'email')

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={
		'type': "text",
		'placeholder': "Введите логин",
		'class': 'form-control border-0 p-3',
	}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'type': "password",
		'placeholder': "Введите пароль",
		'class': 'form-control border-0 p-3',
	}))

	class Meta:
		model = User
		fields = ("username", "password")

class UserBalanceForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('balance',)