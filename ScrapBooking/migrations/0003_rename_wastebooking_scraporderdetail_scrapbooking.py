# Generated by Django 4.2.1 on 2023-06-06 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapBooking', '0002_scraporderdetail_scrapwaste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scraporderdetail',
            old_name='wastebooking',
            new_name='scrapbooking',
        ),
    ]
