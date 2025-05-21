from django import forms
from .models import Course
from .models import Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # Or list specific fields if needed

class StudentForm(forms.ModelForm):
    onay = forms.BooleanField(label="Bu bilgileri kendim doldurdum ve onayliyorum", required=True)

    class Meta:
        model = Student
        fields = ['name', 'student_no', 'email']
        labels = {
            'name': 'Ad Soyad',
            'student_no': 'Öğrenci Numarasi',
            'email': 'E-posta Adresi',
        }

