# Generated by Django 4.2.1 on 2023-06-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=9, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='signup_month',
            field=models.CharField(default=6, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='signup_year',
            field=models.CharField(default=2023, max_length=50),
        ),
    ]