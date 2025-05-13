from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Course
from django.urls import reverse
from datetime import datetime

def index(request):
    return render(request, 'index.html')  

def userlogin(request):
    username = '' 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('empty')
        else:
            messages.error(request, ' Incorrect Entry, Please Try Again..')

    return render(request, 'userlogin.html', {'username': username})

@login_required(login_url='userlogin')
def empty(request):
  courses = Course.objects.all()
  return render(request, 'empty.html', {'courses': courses}) 


@login_required(login_url='userlogin')
def home(request):
    return render(request, 'home.html')  

def userlogout(request):
    logout(request)  
    return redirect('index') 

def password_reset_form(request):
    return render(request,'password_reset_form.html')

def password_reset_done(request):
    return render(request,'password_reset_done.html')

def password_reset_confirm(request):
     return render(request,' password_reset_confirm.html')

def password_reset_complete(request):
     return render(request,' password_reset_complete.html')



def addcourse(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        capacity = request.POST.get('course_capacity')
        code = request.POST.get('course_code')
        date_str = request.POST.get('establishment_date')
        instructor = request.POST.get('instructor')

        try:
            date = datetime.strptime(date_str, '%d.%m.%Y').date()
        except ValueError:
            messages.error(request, 'Tarih formatı yanlış! Lütfen GG.AA.YYYY şeklinde girin.')
            courses = Course.objects.all()
            return render(request, 'addcourse.html', {'courses': courses})

        Course.objects.create(
            course_name=name,
            course_capacity=capacity,
            course_code=code,
            establishment_date=date,
            instructor=instructor
        )
        return redirect('addcourse')  # Sayfayı yenile, yeni kurs eklensin

    # Her GET ve POST işleminden sonra mevcut kursları göster
    courses = Course.objects.all()
    return render(request, 'addcourse.html', {'courses': courses})


def deletecourse(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return redirect('empty')  

    return render(request, 'deletecourse.html', {'courses': courses})


@login_required(login_url='userlogin')
def coursedetail(request, course_id):
    # Kursu al
    course = get_object_or_404(Course, id=course_id)
    update_url = reverse('update', args=[course.id]) 

    return render(request, 'coursedetail.html', {'course': course, 'update_url': update_url})


def student(request,):
    return render(request, 'student.html')


def qr(request,):
    return render(request, 'qr.html')


def update(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Formdan gelen verileri al
        course_name = request.POST.get('course_name', course.course_name)
        course_capacity = request.POST.get('course_capacity', course.course_capacity)
        course_code = request.POST.get('course_code', course.course_code)
        establishment_date = request.POST.get('establishment_date', course.establishment_date)
        instructor = request.POST.get('instructor', course.instructor)

        # Alanları güncelle
        if course_name:
            course.course_name = course_name
        if course_capacity:
            course.course_capacity = course_capacity
        if course_code:
            course.course_code = course_code
        if establishment_date:
            course.establishment_date = establishment_date
        if instructor:
            course.instructor = instructor

        # Değişiklikleri kaydet
        course.save()

        # Güncelleme sonrası yönlendirme
        return redirect('coursedetail', course_id=course.id) 

    return render(request, 'update.html', {'course': course})
