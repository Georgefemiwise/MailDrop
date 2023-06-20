# Generated by Django 4.1.3 on 2023-06-20 10:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year_enrolled',
            field=models.IntegerField(default=2023, verbose_name='Year enrolled'),
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at'),
        ),
    ]
