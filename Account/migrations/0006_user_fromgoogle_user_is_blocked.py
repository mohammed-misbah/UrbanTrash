# Generated by Django 4.2.1 on 2023-06-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_alter_user_signup_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fromGoogle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
