# Generated by Django 4.1.3 on 2025-05-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('code', models.CharField(max_length=20)),
                ('establishment_date', models.CharField(max_length=50)),
                ('instructor', models.CharField(max_length=100)),
            ],
        ),
    ]
