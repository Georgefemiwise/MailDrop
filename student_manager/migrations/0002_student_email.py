# Generated by Django 5.0 on 2023-12-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
