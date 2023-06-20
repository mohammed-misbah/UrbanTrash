# Generated by Django 4.2.1 on 2023-06-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WasteBooking', '0005_alter_wastepickdetail_wastepickup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wastepickup',
            old_name='note',
            new_name='notes',
        ),
        migrations.RemoveField(
            model_name='wastepickup',
            name='weight',
        ),
        migrations.AddField(
            model_name='wastepickup',
            name='waste_weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wastepickup',
            name='pickup_day',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='wastepickup',
            name='pickup_status',
            field=models.CharField(default='pending', max_length=270),
        ),
    ]