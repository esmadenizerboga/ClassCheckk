from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# RollCall'ın urls.py si budur..

urlpatterns = [
    path('', views.home, name='home'), #HOME SAYFASI
    path('giris/', views.giris, name='giris'),  # ClassCheck sayfası
    path('userlogin/', views.userlogin, name='userlogin'),  # Login sayfasıi
    path('userlogout/', views.userlogout, name='userlogout'),   # logout sayfası
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'), #password_reset_form
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('deletecourse/', views.deletecourse, name='deletecourse'),  # deletecourse URL'si
    path('course/<int:course_id>/', views.coursedetail, name='coursedetail'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('update/<int:course_id>/', views.update, name='update'),
    path('qr/', views.qr, name='qr'),
    path('addcourse/', views.addcourse, name='addcourse'),
]
