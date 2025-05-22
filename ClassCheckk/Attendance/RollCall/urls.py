from django.urls import path
from . import views

# RollCall'ın urls.py si budur..

urlpatterns = [
    path('', views.home, name='home'), #HOME SAYFASI
    path('index/', views.index, name='index'),  # ClassCheck sayfası
    path('userlogin/', views.userlogin, name='userlogin'),  # Login sayfasıi
    path('userlogout/', views.userlogout, name='userlogout'),   # logout sayfası
    path('deletecourse/', views.deletecourse, name='deletecourse'),  # deletecourse URL'si
    path('course/<int:course_id>/', views.coursedetail, name='coursedetail'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('update/<int:course_id>/', views.update, name='update'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('take_attendance/', views.take_attendance, name='take_attendance'),
    path('qrgoster/', views.qrgoster, name='qrgoster'),
    path('yoklamalist/', views.yoklamalist, name='yoklamalist'),
    path('yoklama/sil/<int:id>/', views.yoklama_sil, name='yoklama_sil'),
]

