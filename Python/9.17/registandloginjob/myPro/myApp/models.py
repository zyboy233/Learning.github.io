from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import datetime
# 模型一旦发生改变 要重新迁移
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=20,verbose_name='昵称',null=True,blank=True)
    ubirthday = models.DateField(auto_now_add=True,verbose_name='生日',null=True,blank=True)
    uaddress = models.CharField(max_length=200,verbose_name='地址',null=True,blank=True)
    is_login = models.CharField(max_length=5,default=0)

class EmailRecord(models.Model):
    code = models.CharField( max_length=20)
    send_date = models.DateTimeField(default=datetime.datetime.now())
    email = models.EmailField(error_messages={'invalid': '邮箱格式不正确'})

class ResetWithEmail(models.Model):
    email = models.EmailField(error_messages={'invalid':'重置邮箱错误'})