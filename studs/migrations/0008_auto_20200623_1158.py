# Generated by Django 3.0.7 on 2020-06-23 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studs', '0007_auto_20200623_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlocation',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 23, 11, 58, 1, 11914)),
        ),
        migrations.AlterField(
            model_name='classlocation',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 23, 11, 58, 1, 11888)),
        ),
    ]