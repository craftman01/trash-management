# Generated by Django 3.2 on 2023-03-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PID_app', '0029_chatmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_table',
            name='sts',
            field=models.CharField(default='not read', max_length=300),
        ),
    ]
