# Generated by Django 4.2.1 on 2023-06-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0005_alter_adminuser_signup_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='signup_day',
            field=models.CharField(default=16, max_length=50),
        ),
    ]