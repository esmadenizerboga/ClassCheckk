from django import forms
from .models import Course
from .models import QRAttendance

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'  # Or list specific fields if needed


class AttendanceForm(forms.Form):
    name = forms.CharField(
        label="Your Name - Surname",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'})
    )
    student_number = forms.CharField(
        label="Your Student Number",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Number'})
    )
    confirmation = forms.BooleanField(
        label=("EK: I have entered the attendance only on my behalf and acknowledge that I accept any consequences "
               "that may arise under the Harran University Disciplinary Regulations if I sign on behalf of someone else."),
    )
    advice = forms.CharField(
        label=("EK: If you have anything else to add, you can use this section; if not, please leave it blank."),
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter Your Advice'})
    )


class QRAttendanceForm(forms.ModelForm):
    class Meta:
        model = QRAttendance
        fields = ['name', 'student_number', 'confirm', 'advice']
        labels = {
            'name': 'Your Name - Surname',
            'student_number': 'Your Student Number',
            'confirm': (
                'EK: I have entered the attendance only on my behalf and acknowledge that I accept any consequences '
                'that may arise under the Harran University Disciplinary Regulations if I sign on behalf of someone else.'
            ),
            'advice': (
                'EK: If you have anything else to add, you can use this section; if not, please leave it blank.'
            ),
        }