# Generated by Django 4.2.3 on 2023-11-06 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_emails', '0004_alter_smsletter_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsletter',
            name='send_time',
            field=models.TimeField(default=datetime.datetime(2023, 11, 6, 17, 19, 44, 651677, tzinfo=datetime.timezone.utc), verbose_name='Время рассылки'),
        ),
    ]
