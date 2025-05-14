from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Course
from django.urls import reverse
from datetime import datetime
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
import qrcode
from io import BytesIO
import base64



def giris(request):
    courses = Course.objects.all()
    return render(request, 'giris.html', {'courses': courses})

def userlogin(request):
    username = '' 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ' Incorrect Entry, Please Try Again..')

    return render(request, 'userlogin.html', {'username': username})



@login_required(login_url='userlogin')
def home(request):
  courses = Course.objects.all()
  return render(request, 'home.html', {'courses': courses}) 



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
    return redirect('giris') 

def password_reset_form(request):
    return render(request,'password_reset_form.html')

def password_reset_done(request):
    return render(request,'password_reset_done.html')

def password_reset_confirm(request):
     return render(request,' password_reset_confirm.html')

def password_reset_complete(request):
     return render(request,' password_reset_complete.html')



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


#Tarandığında gidilecek hedef sayfanın view'ını tanımla:
def hedef(request):
    return render(request, 'hedef.html')



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



def generateqr(request):
    if request.method == 'POST':
        data = request.POST.get('qr_data')
        
        # QR kod oluştur
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        
        # Görseli hafızaya al (base64 için)
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return render(request, 'generateqr.html', {'qr_code': img_str})

    return render(request, 'generateqr.html')

def qrgiris(reguest):
  return render(reguest,'qrgiris.html') 