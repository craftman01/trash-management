# Generated by Django 3.2 on 2023-04-08 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0035_waste_table_vuname'),
    ]

    operations = [
        migrations.AddField(
            model_name='waste_table',
            name='Status',
            field=models.CharField(default='Not completed', max_length=200),
        ),
    ]