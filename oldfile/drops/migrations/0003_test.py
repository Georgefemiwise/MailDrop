# Generated by Django 4.1.3 on 2022-11-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0002_rename_addresses_bachelorsdegreeaddresses'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]