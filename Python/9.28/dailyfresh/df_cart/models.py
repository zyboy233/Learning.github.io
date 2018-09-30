# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from df_user.models import UserInfo
from df_goods.models import GoodsInfo

from django.db import models

# Create your models here.
# 用户和购物车是一对多，商品和购物车是一对多
class CartInto(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=u'用户')
    goods = models.ForeignKey(GoodsInfo, verbose_name=u'商品')
    count = models.IntegerField(default=0, verbose_name=u'数量')
