# Generated by Django 4.2.1 on 2023-06-21 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapBooking', '0007_alter_scrappickup_pickup_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrappickup',
            name='pickup_day',
            field=models.IntegerField(default=21),
        ),
    ]