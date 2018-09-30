# coding:utf-8
# __author__ = 'Gao'

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.order, name='order'),
    # 提交订单对应的路由
    url(r'^add_order/$', views.add_order, name='add_order'),
]

