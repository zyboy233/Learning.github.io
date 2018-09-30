# Generated by Django 2.1.1 on 2018-09-29 08:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200, verbose_name='图片地址')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsModel', verbose_name='商品')),
            ],
            options={
                'verbose_name_plural': '商品图片',
                'db_table': 'images',
            },
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 29, 16, 48, 30, 837503), verbose_name='创建时间'),
        ),
    ]
