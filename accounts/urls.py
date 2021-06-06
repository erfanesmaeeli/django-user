from django.urls import path
from .views import LoginView
app_name = 'accounts'

urlpatterns = [
	path('login/', LoginView.as_view(), name='login'),
	# path('register/', ..., name='login'),
	# path('logout/', ..., name='login'),
]