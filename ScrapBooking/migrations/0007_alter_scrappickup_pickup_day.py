# Generated by Django 4.2.1 on 2023-06-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapBooking', '0006_rename_note_scrappickup_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrappickup',
            name='pickup_day',
            field=models.IntegerField(default=16),
        ),
    ]