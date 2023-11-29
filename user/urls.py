from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

app_name = 'user'
urlpatterns = [
	path('login/', UserLoginView.as_view(), name='login'),
	path('register/', UserRegistrationView.as_view(), name='register'),
	path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
	path('profile-edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
	path('orders/user-<int:pk>/', OrderListView.as_view(), name='orders'),
	path('order/user-<int:pk>/order-number-<int:order>/', OrderDetailView.as_view(), name='order'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('balance/', UserBalanceView.as_view(), name='balance'),
	path('succless-balance/', SucclessBalanceView.as_view(), name='balance-succless'),
	# path('truereg/', SuccessfulRegistrationView.as_view(), name='truereg'),
]
