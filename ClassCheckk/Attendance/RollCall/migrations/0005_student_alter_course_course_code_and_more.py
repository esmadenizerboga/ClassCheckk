# Generated by Django 4.0.3 on 2025-05-14 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('RollCall', '0004_alter_course_course_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='establishment_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
