# Generated by Django 4.2.1 on 2023-06-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=21, max_length=50),
        ),
    ]
