from django.db import models
from django.contrib import admin
import datetime
# Create your models here.


class SubjectModel(models.Model):
    name = models.CharField(max_length=20,null=False)
    number = models.IntegerField(default=0,null=True)
    days = models.IntegerField(null=False)
    amount = models.CharField(max_length=100,null=False)
    assurance = models.CharField(max_length=100,null=False)
    remark = models.CharField(max_length=100,null=False)
    status = models.CharField(max_length=100,null=True)
    creator = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(default=datetime.datetime.now())
    updater = models.CharField(max_length=100,null=True)
    update_time = models.DateTimeField(default=datetime.datetime.now())
    version = models.IntegerField(default=0, verbose_name='版本')
    class Meta:
        db_table = 'subject'
        verbose_name_plural = '学科'
    def __str__(self):
        return self.name


# @admin.register(SubjectModel)
class SubjectAdminModel(admin.ModelAdmin):
    list_display = ('name','number')
    pass