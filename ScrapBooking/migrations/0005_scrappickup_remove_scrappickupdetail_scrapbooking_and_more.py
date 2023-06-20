# Generated by Django 4.2.1 on 2023-06-12 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_user_signup_day'),
        ('Address', '0001_initial'),
        ('ScrapCategory', '0002_rename_scrapname_scrapwaste_name'),
        ('ScrapBooking', '0004_rename_scraporderdetail_scrappickupdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapPickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=50, max_digits=10)),
                ('pickup_status', models.CharField(default='pending', max_length=20)),
                ('pickup_date', models.DateField()),
                ('pickup_time', models.TimeField()),
                ('note', models.TextField()),
                ('pickup_day', models.IntegerField(default=12)),
                ('pickup_month', models.IntegerField(default=6)),
                ('pickup_year', models.IntegerField(default=2023)),
                ('is_ordered', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Address.address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.user')),
                ('scrapwaste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScrapCategory.scrapcategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='scrappickupdetail',
            name='scrapbooking',
        ),
        migrations.DeleteModel(
            name='ScrapBooking',
        ),
        migrations.AddField(
            model_name='scrappickupdetail',
            name='scrappickup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ScrapBooking.scrappickup'),
            preserve_default=False,
        ),
    ]