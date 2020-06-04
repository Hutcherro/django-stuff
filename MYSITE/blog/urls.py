from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('thanks/', views.detail, name='detail'),
	path('user-login/', views.get_name, name='get_name'),
]