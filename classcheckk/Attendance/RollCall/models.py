from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)  
    course_capacity = models.IntegerField()  
    course_code = models.CharField(max_length=20)  
    establishment_date = models.DateField(null=True, blank=True)
    instructor = models.CharField(max_length=100, blank=True)  

    def __str__(self):
        return self.course_name


