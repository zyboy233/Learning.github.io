# Generated by Django 2.1.1 on 2018-09-27 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20180927_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 20, 50, 9, 484293)),
        ),
        migrations.AlterField(
            model_name='subjectmodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 20, 50, 9, 484293)),
        ),
    ]
