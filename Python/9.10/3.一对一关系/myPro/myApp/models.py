from django.db import models
import time
# Create your models here.
# 一对一关系: 每个人都对应一个身份证 每个身份证都对应一个人
# 如果模型里面的代码发生了更改 那么一定要重新迁移
class One(models.Model):
    # tsub = models.OneToOneField(Two, on_delete=models.CASCADE, primary_key=True)
    oname = models.CharField(max_length=20,null=True)
    oage = models.CharField(max_length=20,null=True)
    # date 日期格式的字段
    odate = models.DateField(null=True)
    # 更改表名
    # class Meta:
    #     db_table = 'first'
class Two(models.Model):
    # 设置一对一关系是通过将表中的字段设置为主键完成的
    # on_delete = models.CASCADE 当父表中的某一条数据删除的时候
    # 相关字表中的数据也会被删除
    # 需要将tsub设置为主键
    tsub = models.OneToOneField(One,on_delete=models.CASCADE,primary_key=True)
    tfond = models.CharField(max_length=20,null=True)
    tdes = models.CharField(max_length=200,null=True)

    # class Meta:
    #     db_table = 'second'


