# Generated by Django 4.2.1 on 2023-06-22 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminSide', '0010_notification_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='type',
        ),
    ]
