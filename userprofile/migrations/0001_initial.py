# Generated by Django 3.2.6 on 2021-09-03 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('education', models.CharField(choices=[('ol', 'O/L'), ('al', 'A/L'), ('diploma', 'Diploma'), ('Bachdeg', "Bachelor's degree"), ('Mastdeg', "Master's degree"), ('phd', 'Phd')], default=None, max_length=50)),
                ('nationality', models.CharField(choices=[('sinhala', 'Sinhala'), ('tamil', 'Tamil'), ('muslim', 'Muslim'), ('other', 'Other')], default=None, max_length=50)),
                ('religion', models.CharField(choices=[('buddhism', 'Buddhism'), ('christian', 'Christian'), ('hindu', 'Hindu'), ('islam', 'Islam'), ('other', 'Other')], default=None, max_length=50)),
                ('skin_complexity', models.CharField(choices=[('very_dark', 'Very dark'), ('dark_brown', 'Dark brown'), ('mid_brown', 'Mid brown'), ('medium', 'Medium'), ('fair', 'Fair'), ('light', 'Light')], default=None, max_length=50)),
                ('eye_color', models.CharField(choices=[('black', 'Black'), ('brown', 'Brown'), ('blue', 'Blue'), ('gray', 'Gray'), ('hazel', 'Hazel')], default=None, max_length=50)),
                ('occupation', models.CharField(choices=[('government', 'Government'), ('private', 'Private')], default=None, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatnertBio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('salary', models.FloatField()),
                ('education', models.CharField(choices=[('ol', 'O/L'), ('al', 'A/L'), ('diploma', 'Diploma'), ('Bachdeg', "Bachelor's degree"), ('Mastdeg', "Master's degree"), ('phd', 'Phd')], max_length=50)),
                ('nationality', models.CharField(choices=[('sinhala', 'Sinhala'), ('tamil', 'Tamil'), ('muslim', 'Muslim'), ('other', 'Other')], max_length=50)),
                ('religion', models.CharField(choices=[('buddhism', 'Buddhism'), ('christian', 'Christian'), ('hindu', 'Hindu'), ('islam', 'Islam'), ('other', 'Other')], max_length=50)),
                ('skin_complexity', models.CharField(choices=[('very_dark', 'Very dark'), ('dark_brown', 'Dark brown'), ('mid_brown', 'Mid brown'), ('medium', 'Medium'), ('fair', 'Fair'), ('light', 'Light')], max_length=50)),
                ('eye_color', models.CharField(choices=[('black', 'Black'), ('brown', 'Brown'), ('blue', 'Blue'), ('gray', 'Gray'), ('hazel', 'Hazel')], max_length=50)),
                ('occupation', models.CharField(choices=[('government', 'Government'), ('private', 'Private')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]