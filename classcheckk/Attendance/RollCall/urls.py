from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# RollCall'ın urls.py si budur..

urlpatterns = [
    path('', views.home, name='home'),  # Home Sayfasına Geçecek
    path('index/', views.index, name='index'),  # ClassCheck sayfası
    path('userlogin/', views.userlogin, name='userlogin'),  # Login sayfasıi
    path('empty/', views.empty, name='empty'),  # Empty Sayfasi
    path('userlogout/', views.userlogout, name='userlogout'),   # logout sayfası
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'), #password_reset_form
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('deletecourse/', views.deletecourse, name='deletecourse'),
    path('course/<int:course_id>/', views.coursedetail, name='coursedetail'),
    path('student/', views.student, name='student'),
    path('qr/', views.qr, name='qr'),
    path('update/<int:course_id>/', views.update, name='update')

]
