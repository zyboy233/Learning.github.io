# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetailinfo',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
