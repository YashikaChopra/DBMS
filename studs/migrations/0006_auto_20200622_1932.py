# Generated by Django 3.0.7 on 2020-06-22 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studs', '0005_auto_20200622_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlocation',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 22, 19, 32, 17, 309426)),
        ),
        migrations.AlterField(
            model_name='classlocation',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 22, 19, 32, 17, 309374)),
        ),
    ]
