# Generated by Django 4.2.1 on 2024-01-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WasteBooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wastepickup',
            name='pickup_day',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='wastepickup',
            name='pickup_month',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wastepickup',
            name='pickup_year',
            field=models.IntegerField(default=2024),
        ),
    ]
