# Generated by Django 3.2 on 2023-04-08 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0036_waste_table_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_reg',
            name='Interests',
        ),
        migrations.RemoveField(
            model_name='customer_reg',
            name='Rating',
        ),
    ]