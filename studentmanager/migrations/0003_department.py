# Generated by Django 4.2.2 on 2023-06-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanager', '0002_remove_program_department_remove_student_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='computer science ', max_length=30, verbose_name='department name')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
    ]
