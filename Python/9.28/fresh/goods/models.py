import datetime

from django.db import models
from django.contrib import admin
from user.models import UserModel
# Create your models here.

class CategoryModel(models.Model):
    """商品分类模型"""
    category_name = models.CharField(max_length=20,null=False,verbose_name='商品分类名称')
    # 排序
    number = models.IntegerField(default=0,verbose_name='排序',unique=True,null=False)
    # 分类的图片
    image = models.CharField(default='/static/images/banner01',max_length=100,null=False,verbose_name='分类的展示图片')
    class Meta:
        db_table = 'category'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.category_name

@admin.register(CategoryModel)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('category_name',)

class GoodsModel(models.Model):
    """商品模型"""
    # 商品名称
    goods_name = models.CharField(max_length=50,null=False,verbose_name='商品名称')
    # 商品简介
    abstract = models.CharField(max_length=200,null=True,verbose_name='商品简介')
    # 价格
    # max_digits,总长度  ; decimal_places 小数点后位数
    price = models.DecimalField(default=0,max_digits=11,decimal_places=2)
    # 单位
    unit = models.CharField(max_length=20,null=False,verbose_name='商品售卖单位')
    # 库存
    stock = models.IntegerField(default=0,verbose_name='库存')
    # 详细介绍
    desc = models.TextField(null=True,verbose_name='详细介绍')
    # 默认图片
    pic = models.CharField(default='/static/images/goods/goods003.jpg',null=False,max_length=200,verbose_name='商品默认图片')

    # 添加一个分类的外键
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,verbose_name='商品分类',default=1,null=False)
    # 人气
    popular = models.IntegerField(default=0,null=False,verbose_name='人气指数')

    class Meta:
        # 自定义表名
        db_table = 'goods'
        verbose_name_plural = '商品信息'
    def __str__(self):
        # 对象名字
        return self.goods_name

@admin.register(GoodsModel)
class GoodsAdminModel(admin.ModelAdmin):
    """商品注册管理后台"""
    list_display = ['goods_name','stock','price','category']



class CommentModel(models.Model):
    """评论模型"""
    # 用户对评论一对多的关系
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE,verbose_name='评论的用户')
    # 商品跟评论的一对多的关系
    goods_id = models.ForeignKey(GoodsModel,on_delete=models.CASCADE,verbose_name='商品')
    # 评论的内容
    content = models.CharField(max_length=256,null=False,verbose_name='评论的内容')
    # 被点赞的次数
    vote_number = models.IntegerField(default=0,verbose_name='点赞数')
    # 创建时间
    create_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')

    class Meta:
        db_table = 'comment'
        verbose_name_plural = '评论'

@admin.register(CommentModel)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ('goods_id','user_id','content','vote_number','create_time')

class ImagesModel(models.Model):
    """存储图片与商品的关系"""
    goods = models.ForeignKey(GoodsModel,on_delete=models.CASCADE,verbose_name='商品')
    #
    image_url = models.CharField(max_length=200,verbose_name='图片地址',null=False)

    class Meta:
        db_table = 'images'
        verbose_name_plural = '商品图片'

@admin.register(ImagesModel)
class ImagesAdminModel(admin.ModelAdmin):
    list_display = ('goods','image_url')

class CategoryGoodsModel(models.Model):
    """商品分类和商品之间的关系"""
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,verbose_name='商品分类')
    goods = models.ForeignKey(GoodsModel,on_delete=models.CASCADE,verbose_name='商品')

    class Meta:
        db_table = 'category_goods'
        verbose_name_plural = '商品分类和商品关系'

@admin.register(CategoryGoodsModel)
class CategoryGoodsAdminModel(admin.ModelAdmin):
    list_display = ('category','goods')