# Generated by Django 4.2.1 on 2023-06-07 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScrapCategory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapwaste',
            old_name='scrapname',
            new_name='name',
        ),
    ]
