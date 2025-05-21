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
    path('StudentForm/', views.StudentForm, name='StudentForm'),
]
