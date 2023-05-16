# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-07-14 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=40)),
                ('b_address', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=20)),
                ('number_of_steps', models.CharField(max_length=20)),
            ],
        ),
    ]