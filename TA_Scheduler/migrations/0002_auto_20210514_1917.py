# Generated by Django 3.1.7 on 2021-05-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TA_Scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor_lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
