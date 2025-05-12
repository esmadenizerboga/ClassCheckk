from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Course


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
        date = request.POST.get('establishment_date')
        instructor = request.POST.get('instructor')

        Course.objects.create(
            name=name,
            capacity=capacity,
            code=code,
            establishment_date=date,
            instructor=instructor
        )
        return redirect('empty')  # empty adlı sayfaya yönlendir
    return render(request, 'addcourse.html')  # add_course.html adında bir form sayfası


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
    return render(request, 'coursedetail.html')


def student(request,):
    return render(request, 'student.html')


def qr(request,):
    return render(request, 'qr.html')