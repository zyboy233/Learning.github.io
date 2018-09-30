# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from df_user.models import UserInfo
from df_goods.models import GoodsInfo

from django.db import models

# Create your models here.
# 关于订单的模型(orderinfo)：订单编号、订单id、订单日期、订单是否支付等；
# 关于订单中商品的模型(orderdetailinfo)：订单都包含哪些商品
# orderinfo和orderdetailinfo是一对多的关系

class OrderInfo(models.Model):
    o_id = models.CharField(max_length=100, primary_key=True, verbose_name=u'订单编号')
    o_date = models.DateTimeField(auto_now=True, verbose_name=u'订单日期')
    o_pay = models.BooleanField(default=False, verbose_name=u'是否支付')
    o_total_price = models.CharField(max_length=100, verbose_name=u'订单总金额')
    # 用户和订单之间是一对多关系
    user = models.ForeignKey(UserInfo)

class OrderDetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)
    # 订单详情和商品之间是一对多的关系
    goods = models.ForeignKey(GoodsInfo)
    # 购买数量
    count = models.IntegerField(default=0)

