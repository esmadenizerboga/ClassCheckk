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



class Yoklama(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    numara = models.CharField(max_length=20)
    onaylandi = models.BooleanField(default=False)  # kutucuk: "kendim onayladım"

    def __str__(self):
        durum = "APPROVED" if self.onaylandi else "NOT APPROVED"
        return f"{self.ad} {self.soyad} - {self.numara} ({durum})"



