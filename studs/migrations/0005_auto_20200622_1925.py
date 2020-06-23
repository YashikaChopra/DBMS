# Generated by Django 3.0.7 on 2020-06-22 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studs', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='classlocation',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 22, 19, 25, 13, 930056)),
        ),
        migrations.AddField(
            model_name='classlocation',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 22, 19, 25, 13, 930029)),
        ),
        migrations.AlterField(
            model_name='classlocation',
            name='NameOfClass',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]