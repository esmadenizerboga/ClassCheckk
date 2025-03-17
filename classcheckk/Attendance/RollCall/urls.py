from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa
    path('login/', views.login_view, name='login'),  # Giriş sayfası
    path('courses/', views.course_list, name='course_list'),  # Ders listesi
    path('attendance/<int:course_id>/', views.attendance_view, name='RollCall'),  # Devam takip sayfası
]