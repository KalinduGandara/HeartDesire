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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality_id', models.IntegerField()),
                ('nic', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], default=None, max_length=20)),
                ('rel_stats', models.CharField(choices=[('single', 'Singal'), ('married', 'Married'), ('divorced', 'Divorced'), ('seperated', 'Seperated'), ('widow', 'Widow')], default=None, max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('about', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]