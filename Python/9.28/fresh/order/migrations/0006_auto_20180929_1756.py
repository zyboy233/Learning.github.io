# Generated by Django 2.1.1 on 2018-09-29 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20180929_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 17, 56, 24, 911533), verbose_name='订单创建时间'),
        ),
    ]
