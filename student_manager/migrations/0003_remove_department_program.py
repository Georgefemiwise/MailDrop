# Generated by Django 4.2.2 on 2023-09-11 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_manager', '0002_alter_department_created_at_alter_department_faculty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='program',
        ),
    ]
