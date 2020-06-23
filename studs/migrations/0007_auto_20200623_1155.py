# Generated by Django 3.0.7 on 2020-06-23 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studs', '0006_auto_20200622_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlocation',
            name='roomno',
            field=models.CharField(default='LC1', max_length=50),
        ),
        migrations.AlterField(
            model_name='classlocation',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 23, 11, 55, 13, 684604)),
        ),
        migrations.AlterField(
            model_name='classlocation',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 23, 11, 55, 13, 684577)),
        ),
    ]