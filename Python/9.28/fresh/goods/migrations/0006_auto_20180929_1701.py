# Generated by Django 2.1.1 on 2018-09-29 09:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20180929_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.CategoryModel', verbose_name='商品分类')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsModel', verbose_name='商品')),
            ],
            options={
                'verbose_name_plural': '商品分类和商品关系',
                'db_table': 'category_goods',
            },
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 17, 1, 54, 593709), verbose_name='创建时间'),
        ),
    ]
