# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# 引入第三方的富文本编辑器，支持HTML语法。
from tinymce.models import HTMLField

# Create your models here.

# 商品分类模型
class TypeInfo(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'分类名称')

    def __str__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = u'分类名称'
        verbose_name_plural = u'分类名称'

# 商品信息模型
class GoodsInfo(models.Model):
    # 商品名称
    g_title = models.CharField(max_length=100, verbose_name=u'商品名称')
    # 商品图片地址
    g_pic = models.ImageField(upload_to='df_goods', verbose_name=u'商品图片')
    # 商品单价 DecimalField可以设置价格的小数位位数。
    # max_digits=7 价格总共有几位数 99999.99
    # decimal_places=2 小数点保留两位
    g_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=u'商品价格')
    # 商品计价单位
    g_unit = models.CharField(max_length=50, verbose_name=u'计量单位')
    # 商品的浏览次数，用于人气排序
    g_click = models.IntegerField(verbose_name=u'浏览次数')
    # 商品的简介
    g_abstract = models.CharField(max_length=255, verbose_name=u'商品简介')
    # 商品的库存
    g_stock = models.IntegerField(verbose_name=u'商品库存')
    # 商品的详细介绍
    g_content = HTMLField(verbose_name=u'商品详细介绍')

    # 商品类型和商品之间是一对多的关系，forginkey()设置在 "多" 的一方
    g_type = models.ForeignKey(TypeInfo, verbose_name=u'分类')

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品'

    def __str__(self):
        return self.g_title.encode('utf-8')