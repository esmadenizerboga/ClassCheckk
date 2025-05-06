from django.urls import path
from . import views
# RollCall'ın urls.py si budur..
urlpatterns = [
    path('', views.home, name='home'),  # Home Sayfasına Geçecek
    path('index/', views.index, name='index'),  # ClassCheck sayfası
    path('userlogin/', views.userlogin, name='userlogin'),  # Login sayfası
    path('empty/', views.empty, name='empty'),  # Empty Sayfasi
    path('userlogout/', views.userlogout, name='userlogout'),   # logout sayfası
]