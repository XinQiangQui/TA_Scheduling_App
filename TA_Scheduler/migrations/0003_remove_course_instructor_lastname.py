# Generated by Django 3.1.7 on 2021-05-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduler', '0002_auto_20210514_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor_lastname',
        ),
    ]
