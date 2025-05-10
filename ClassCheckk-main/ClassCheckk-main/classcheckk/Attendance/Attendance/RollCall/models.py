from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    code = models.CharField(max_length=20)
    establishment_date = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # empty sayfasında sadece ismi gösterir

