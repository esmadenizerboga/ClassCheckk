from django.db import models
from django.utils import timezone

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_capacity = models.IntegerField()
    course_code = models.CharField(max_length=20)
    establishment_date = models.DateField(default=timezone.now)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_no = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone

class QRAttendance(models.Model):
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20)
    confirm = models.BooleanField()
    advice = models.TextField(blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.student_number}"

