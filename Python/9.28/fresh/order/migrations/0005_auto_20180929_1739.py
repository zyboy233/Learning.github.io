# Generated by Django 2.1.1 on 2018-09-29 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20180929_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 17, 39, 37, 539812), verbose_name='订单创建时间'),
        ),
    ]
