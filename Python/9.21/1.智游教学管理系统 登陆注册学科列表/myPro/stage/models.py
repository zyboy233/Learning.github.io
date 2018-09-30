from django.db import models
from django.contrib import admin
from subject.models import SubjectModel
import datetime
# Create your models here.

class StageModel(models.Model):
    subjects = SubjectModel.objects.all()
    subject_name_id = [(subject.id,subject.name) for subject in subjects]
    subject_id = models.IntegerField(default=0,verbose_name='学科编号',choices=subject_name_id)
    title = models.CharField(max_length=50,verbose_name='阶段')
    number = models.IntegerField(default=0,null=True,verbose_name='排序')
    days = models.IntegerField(null=False)
    project = models.CharField(max_length=255,verbose_name='项目')
    teaching = models.CharField(max_length=255,verbose_name='教学方法')
    learning = models.CharField(max_length=255,verbose_name='学习方法')
    sharing = models.CharField(max_length=255,verbose_name='学生分享')
    remark = models.CharField(max_length=100, null=True,verbose_name='备注')
    status = models.CharField(max_length=100, null=True,verbose_name='状态')
    creator = models.CharField(max_length=100, null=True,verbose_name='创建者')
    create_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    updater = models.CharField(max_length=100, null=True,verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')
    version = models.IntegerField(default=0, verbose_name='版本')

    class Meta:
        verbose_name_plural='阶段'

    def __str__(self):
        return self.title

@admin.register(StageModel)
class StageAdminModel(admin.ModelAdmin):
    list_display = ('title',)
