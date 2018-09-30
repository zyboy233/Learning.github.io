from django.db import models
from django.contrib import admin
# Create your models here.

class UserModel(models.Model):
    """创建用户的model"""

    # 用户名
    username = models.CharField(max_length=50,null=False,verbose_name='用户名')
    # 密码
    password = models.CharField(max_length=256,null=False,verbose_name='密码')
    # 电话
    phone = models.CharField(max_length=11,null=False,verbose_name='电话号码')
    # 地址 blank 值为true的时候代表后台可以不用填写这个值
    address = models.CharField(max_length=200,null=True,blank=True,verbose_name='收货地址')
    # 电子邮箱
    email = models.EmailField(verbose_name='电子邮箱',blank=True,null=True)
    class Meta:
        db_table = 'user'
        # 修改后台显示
        verbose_name_plural = '用户'
    def __str__(self):
        return self.username

@admin.register(UserModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['username','phone','address']

class CollectGoodsModel(models.Model):
    """收货地址和信息管理"""
    # 属于谁的收货信息
    # 用户对收货信息是一对多的关系
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    # 收件人
    person_name = models.CharField(max_length=30,verbose_name='收件人',null=False)
    # 详细地址
    detail_address = models.CharField(max_length=200,verbose_name='详细地址',null=True)
    # 邮政编码
    postcode = models.IntegerField(default=000000,verbose_name='邮政编码')
    # 联系方式
    tel = models.CharField(max_length=20,verbose_name='联系方式',null=True)
    # 是否正在使用
    is_used = models.BooleanField(verbose_name='是否正在使用')
    class Meta:
        db_table = 'CollectGoods'
        verbose_name_plural = '收货信息管理'
    def __str__(self):
        return self.person_name

# 在admin.py里应该这样添加 和装饰器的admin只能保留一个
# admin.site.register(CollectGoodsModel,CollectGoodsAdminModel)
@admin.register(CollectGoodsModel)
class CollectGoodsAdminModel(admin.ModelAdmin):
    """把收件信息注册到管理后台"""
    list_display = ['person_name','tel','detail_address','is_used']