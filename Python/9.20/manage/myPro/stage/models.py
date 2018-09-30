from django.db import models
from myApp.models import Subject
import datetime
# Create your models here.

class Stage(models.Model):
    subjects = Subject.objects.all()
    subject_name_id = [(subject.id,subject.name) for subject in subjects]
    subject_id = models.IntegerField(default=0,verbose_name='阶段id',choices=subject_name_id)
    title = models.CharField(max_length=50,null=False)
    days = models.IntegerField(null=False)
    number = models.IntegerField(null=True)
    project = models.CharField(max_length=255,null=True)
    teaching = models.CharField(max_length=255,null=True)
    learning = models.CharField(max_length=255)
    sharing = models.CharField(max_length=255)
    remark = models.CharField(max_length=100, null=True,verbose_name='备注')
    status = models.CharField(max_length=100, null=True,verbose_name='状态')
    creator = models.CharField(max_length=100, null=True,verbose_name='创建者')
    create_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    updater = models.CharField(max_length=100, null=True,verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')
    class Meta:
        db_table = 'stage'
        verbose_name_plural='阶段'
    def __str__(self):
        return self.title
