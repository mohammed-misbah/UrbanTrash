# Generated by Django 4.2.1 on 2023-06-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_user_signup_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=15, max_length=50),
        ),
    ]