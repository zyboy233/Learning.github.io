# Generated by Django 2.1.1 on 2018-09-29 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20180929_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 17, 39, 37, 523822), verbose_name='创建时间'),
        ),
    ]
