# Generated by Django 4.0.3 on 2025-05-20 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RollCall', '0005_student_alter_course_course_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_number', models.CharField(max_length=20)),
                ('confirm', models.BooleanField()),
                ('advice', models.TextField(blank=True)),
                ('submitted_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
