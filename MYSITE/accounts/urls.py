from django.urls import path

from .import views

urlpatterns = [
    path('', views.home),
    path('account/login/', views.login_view),
    #path('')
]