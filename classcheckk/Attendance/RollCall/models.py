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



