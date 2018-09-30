from django.db import models
from stage.models import StageModel
from django.contrib import admin
import datetime
# Create your models here.

class OutlineModel(models.Model):
    stages = StageModel.objects.all()
    stage_id_title = [(stage.id,stage.title) for stage in stages]
    stage_id = models.IntegerField(default=0,verbose_name='阶段id',choices=stage_id_title)
    number = models.IntegerField(default=0,null=True)
    title = models.CharField(max_length=255,null=True,verbose_name='标题')
    days = models.IntegerField(default=0,null=True,verbose_name='学时')
    advancing = models.CharField(max_length=255,null=True,verbose_name='高级内容')
    remark = models.CharField(max_length=255,null=True,verbose_name='备注')
    status = models.CharField(max_length=100, null=True, verbose_name='状态')
    creator = models.CharField(max_length=100, null=True, verbose_name='创建者')
    create_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间')
    updater = models.CharField(max_length=100, null=True, verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')
    version = models.IntegerField(default=0,verbose_name='版本')
    class Meta:
        db_table = 'outline'
        verbose_name_plural='一级大纲'
    def __str__(self):
        return self.title
@admin.register(OutlineModel)
class OutlineAdminModel(admin.ModelAdmin):
    list_display = ('title','days')
