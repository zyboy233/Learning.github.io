from django.db import models
from django.contrib import admin
from stage.models import StageModel
from outline.models import OutlineModel
import datetime
# Create your models here.

class ProgramModel(models.Model):
    stages = StageModel.objects.all()
    stage_id_title = [(stage.id, stage.title) for stage in stages]
    outlines = OutlineModel.objects.all()
    outline_id_title = [(outline.id,outline.title) for outline in outlines]
    stage_id = models.IntegerField(default=0, verbose_name='阶段id', choices=stage_id_title)
    outline_id = models.IntegerField(default=0,verbose_name='大纲id',choices=outline_id_title)
    number = models.IntegerField(default=0, null=True)
    sign = models.CharField(max_length=50,null=True,verbose_name='标志')
    digest = models.CharField(max_length=255,null=True,verbose_name='内容摘要')
    prepare = models.CharField(max_length=255,null=True,verbose_name='准备')
    process = models.CharField(max_length=2000,null=True,verbose_name='讲课流程')
    attention = models.CharField(max_length=255,null=True,verbose_name='注意事项')
    exercise = models.CharField(max_length=255,null=True,verbose_name='练习')
    share = models.CharField(max_length=255,null=True,verbose_name='分享')
    management = models.CharField(max_length=255,null=True,verbose_name='管理事项')
    remark = models.CharField(max_length=255, null=True, verbose_name='备注')
    status = models.CharField(max_length=100, null=True, verbose_name='状态')
    creator = models.CharField(max_length=100, null=True, verbose_name='创建者')
    create_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间')
    updater = models.CharField(max_length=100, null=True, verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')
    version = models.IntegerField(default=0, verbose_name='版本')
    class Meta:
        db_table='program'
        verbose_name_plural='二级大纲'

@admin.register(ProgramModel)
class ProgramAdminModel(admin.ModelAdmin):
    list_display = ('sign',)