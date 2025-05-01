from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home Sayfasına Geçecek
    path('index/', views.index, name='index'),  # ClassCheck sayfası
    path('userlogin/', views.userlogin, name='userlogin'),  # Login sayfası
    path('empty/', views.empty, name='empty'),  # Empty Sayfasi
    path('userlogout/', views.userlogout, name='userlogout'),   # logout sayfası
]