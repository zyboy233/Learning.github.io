from django.db import models

# Create your models here.
class Person(models.Model):
    # AutoField设置自动增加
    # 设置是否为主键
    uid = models.AutoField(primary_key=True)
    # 设置字段是否可以为空
    uname = models.CharField(max_length=100,null=True)

    uage = models.IntegerField(null=True)
    # 设置字段类型为bool类型
    usex = models.NullBooleanField()