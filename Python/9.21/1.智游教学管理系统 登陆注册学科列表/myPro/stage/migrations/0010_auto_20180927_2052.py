# Generated by Django 2.1.1 on 2018-09-27 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0009_auto_20180927_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagemodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 20, 52, 31, 461455), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='stagemodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 20, 52, 31, 461455), verbose_name='更新时间'),
        ),
    ]
