# Generated by Django 3.0.7 on 2020-06-14 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studs', '0003_auto_20200609_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=60)),
            ],
        ),
    ]
