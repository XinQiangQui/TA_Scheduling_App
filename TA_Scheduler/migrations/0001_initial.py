# Generated by Django 3.1.7 on 2021-05-14 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('lastname', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('home_address', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(default='123', max_length=20)),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, null=True)),
                ('startDate', models.DateField(null=True)),
                ('endDate', models.DateField(null=True)),
                ('content', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cId', models.IntegerField(null=True)),
                ('semester', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=30, null=True)),
                ('lab_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_num', models.IntegerField(blank=True, null=True)),
                ('office_hours', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('instructorOrTa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_Scheduler.account')),
            ],
        ),
    ]
