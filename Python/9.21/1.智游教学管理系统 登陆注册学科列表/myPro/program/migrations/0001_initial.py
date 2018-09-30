# Generated by Django 2.1.1 on 2018-09-26 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_id', models.IntegerField(choices=[(1, '阶段1'), (2, '阶段1'), (3, '阶段2'), (5, '阶段1'), (7, '阶段3'), (8, '阶段2'), (9, '阶段3'), (10, '阶段4')], default=0, verbose_name='阶段id')),
                ('outline_id', models.IntegerField(choices=[(1, '平凡的世界'), (2, '大纲标题1号'), (3, '大纲标题2号'), (7, '大纲2')], default=0, verbose_name='大纲id')),
                ('number', models.IntegerField(default=0, null=True)),
                ('sign', models.CharField(max_length=50, null=True, verbose_name='标志')),
                ('digest', models.CharField(max_length=255, null=True, verbose_name='内容摘要')),
                ('prepare', models.CharField(max_length=255, null=True, verbose_name='准备')),
                ('process', models.CharField(max_length=2000, null=True, verbose_name='讲课流程')),
                ('attention', models.CharField(max_length=255, null=True, verbose_name='注意事项')),
                ('exercise', models.CharField(max_length=255, null=True, verbose_name='练习')),
                ('share', models.CharField(max_length=255, null=True, verbose_name='分享')),
                ('management', models.CharField(max_length=255, null=True, verbose_name='管理事项')),
                ('remark', models.CharField(max_length=255, null=True, verbose_name='备注')),
                ('status', models.CharField(max_length=100, null=True, verbose_name='状态')),
                ('creator', models.CharField(max_length=100, null=True, verbose_name='创建者')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 9, 26, 15, 55, 59, 900980), verbose_name='创建时间')),
                ('updater', models.CharField(max_length=100, null=True, verbose_name='更新者')),
                ('update_time', models.DateTimeField(default=datetime.datetime(2018, 9, 26, 15, 55, 59, 900980), verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '二级大纲',
                'db_table': 'program',
            },
        ),
    ]
