# Generated by Django 3.2 on 2023-03-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0020_booking_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_reg',
            name='Rating',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='driver_reg',
            name='Rating',
            field=models.CharField(default='0', max_length=200),
        ),
    ]