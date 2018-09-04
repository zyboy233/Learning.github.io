from django.db import models

# Create your models here.

class First(models.Model):
    # char 字符  unique 唯一
    # 模型里面的所有类 都是Django.db.models的子类
    # 这些类在数据库中会被转化成数据表
    # 类中的所有字段都是django.db.models.Field的子类
    # 所有字段在数据中会被转化成数据库字段
    name = models.CharField(max_length=300,unique=True)
    des = models.CharField(max_length=200)

    def __str__(self):
        return self.name