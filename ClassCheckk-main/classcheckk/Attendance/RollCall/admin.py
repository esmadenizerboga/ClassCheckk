from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_capacity', 'course_code', 'establishment_date', 'instructor')
    list_filter = ('establishment_date',)
