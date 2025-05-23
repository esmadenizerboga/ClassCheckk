from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Course
from django.urls import reverse
from django.shortcuts import render
from .models import Student
from .models import Yoklama
from django.views.decorators.http import require_POST



def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def userlogin(request):
    username = '' 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get('remember_me')
        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if remember:
                # Remember Me işaretliyse, oturumu uzun tut (örneğin 5 dakika)
                request.session.set_expiry(300)  # 5 dakika
            else:
                # İşaretli değilse, oturumu tarayıcı kapanana kadar tut
                request.session.set_expiry(0)

            return redirect('home')
        else:
            messages.error(request, ' Incorrect Entry, Please Try Again..')

    return render(request, 'userlogin.html', {'username': username})


@login_required(login_url='userlogin')
def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses}) 


@login_required(login_url='userlogin')
def addcourse(request, course_id=None):  # course_id opsiyonel parametre
    if course_id:  # Eğer course_id varsa, mevcut kursu al
        course = get_object_or_404(Course, id=course_id)
    else:
        course = None  # Yeni kurs eklemek için

    if request.method == 'POST':
        # Formdan gelen verileri al
        course_name = request.POST.get('course_name')
        course_capacity = request.POST.get('course_capacity')
        course_code = request.POST.get('course_code')
        establishment_date = request.POST.get('establishment_date')
        instructor = request.POST.get('instructor')

        # Yeni kurs ekleme
        if not course:
            course = Course(
                course_name=course_name,
                course_capacity=course_capacity,
                course_code=course_code,
                establishment_date=establishment_date,
                instructor=instructor
            )
            course.save()  # Kursu kaydet
        
        return redirect('home')

    return render(request, 'addcourse.html', {'course': course})


def userlogout(request):
    logout(request)  
    return redirect('index') 


@login_required(login_url='userlogin')
def deletecourse(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return redirect('home')  

    return render(request, 'deletecourse.html', {'courses': courses}) 


@login_required(login_url='userlogin')
def coursedetail(request, course_id):
    # Kursu al
    course = get_object_or_404(Course, id=course_id)
    update_url = reverse('update', args=[course.id]) 

    return render(request, 'coursedetail.html', {'course': course, 'update_url': update_url})


@login_required(login_url='userlogin')
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


@login_required(login_url='userlogin')
def addstudent(request):
    if request.method == 'POST':
        # Öğrenci ekleme
        if 'add_student' in request.POST:
            name = request.POST.get('name')
            student_no = request.POST.get('student_no')
            email = request.POST.get('email')

            if name and student_no and email:
                student = Student(name=name, student_no=student_no, email=email)
                student.save()

            else:
                return render(request, 'addstudent.html', {
                    'error': 'Tüm alanları doldurmalısınız.'
                })

        # Öğrenci silme
        elif 'delete_student' in request.POST:
            student_id = request.POST.get('student_id')
            student = get_object_or_404(Student, id=student_id)
            student.delete()

        # Öğrenciler listele
        students = Student.objects.all()
        return render(request, 'addstudent.html', {
            'students': students,
        })

    # GET isteği olduğunda öğrencileri listele
    students = Student.objects.all()
    return render(request, 'addstudent.html', {
        'students': students,
    })

def qrgoster(request):
    return render(request, 'qrgoster.html')

def take_attendance(request):
    if request.method == 'POST':
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        numara = request.POST.get('numara')
        onaylandi = request.POST.get('onaylandi') == 'on'  # Checkbox kontrolü

        # Yoklama veritabanına kaydet
        Yoklama.objects.create(ad=ad, soyad=soyad, numara=numara, onaylandi=onaylandi)
        
        return render(request, 'yoklamateyit.html')  # Başarılı sayfa
    
    return render(request, 'yoklama_alindi.html')  # Form sayfası




def yoklamalist(request):
    yoklamalar = Yoklama.objects.all().order_by('-id')  # Tüm yoklamalar, yeni ilk
    return render(request, 'yoklamalist.html', {'yoklamalar': yoklamalar})

@require_POST
def yoklama_sil(request, id):
    yoklama = get_object_or_404(Yoklama, id=id)
    yoklama.delete()
    return redirect('yoklamalist')  # yoklama listesi sayfasının url name'i
