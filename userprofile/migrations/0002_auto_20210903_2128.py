# Generated by Django 3.2.6 on 2021-09-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patnertbio',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patnertbio',
            name='height',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patnertbio',
            name='salary',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patnertbio',
            name='weight',
            field=models.CharField(max_length=50),
        ),
    ]
