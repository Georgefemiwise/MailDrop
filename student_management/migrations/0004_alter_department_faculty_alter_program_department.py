# Generated by Django 4.2.2 on 2023-09-05 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0003_faculty_alter_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management.faculty'),
        ),
        migrations.AlterField(
            model_name='program',
            name='department',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='student_management.department'),
        ),
    ]
