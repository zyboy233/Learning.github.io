from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class MyUser(AbstractUser):
    nickname = models.CharField(max_length=20,verbose_name='昵称',null=True,blank=True)
    class Meta:
        db_table = 'MyUser'
class EmailRecord(models.Model):
    code = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.datetime.now())
    email = models.EmailField(error_messages={'invalid':'邮箱格式不正确'})
    class Meta:
        db_table = 'emailrecord'