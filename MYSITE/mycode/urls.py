from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name='index'),
	path('shop-offer/', views.ShopView, name='ShopView')
]
