# Generated by Django 4.1.3 on 2022-11-26 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
