# Generated by Django 4.2.1 on 2023-06-09 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_user_signup_day_user_signup_month_user_signup_year'),
        ('WasteCategory', '0002_rename_wastename_biowaste_name'),
        ('Address', '0001_initial'),
        ('WasteBooking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WasteOrderDetail',
            new_name='WastePickDetail',
        ),
    ]
