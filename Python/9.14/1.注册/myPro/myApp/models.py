from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 在django里面有一些内置表,内置表会包含一些基本数据字段
# 其中有一个叫做auth_user类,里面默认包含了用户信息,比如账号 密码等
# 因为这个类不能修改  所以可以创建一个模型继承自这个类 使用这个模型进行
# 用户的存储 auth_user类中使用的基础类为AbstractUser

class CustomUser(AbstractUser):
    # AbstractUser 里面有默认字段 可以全部使用默认字段 也可以添加额外字段
    # 以下是添加的额外字段  这些字段只做演示 代码其他地方用不到
    birthday = models.DateField(default='2015-08-12')
    nick = models.CharField(max_length=100,default='honey')
    class Meta:
        db_table = 'my_user'