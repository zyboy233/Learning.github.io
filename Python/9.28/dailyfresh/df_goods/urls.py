# coding:utf-8
# __author__ = 'Gao'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # 商品列表页的路由
    url(r'^list/(\d+)/(\d+)/(\w+)/$', views.goodslist),
    # 详情页的路由
    url(r'^(\d+)/$', views.detail),
]
