# Generated by Django 4.2.1 on 2023-06-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('password', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('signup_day', models.CharField(default=9, max_length=50)),
                ('signup_month', models.CharField(default=6, max_length=50)),
                ('signup_year', models.CharField(default=2023, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
