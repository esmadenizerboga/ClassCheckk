from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_capacity', 'course_code', 'establishment_date', 'instructor']

admin.site.register(Course, CourseAdmin)

