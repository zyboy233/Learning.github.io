# coding:utf-8
# __author__ = 'Gao'

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.cart),
    # 添加购物车路由
    url(r'^add/(\d+)/(\d+)/$', views.add),
    # 修改购物车商品数量路由
    url(r'^update/(\d+)/(\d+)/$', views.update),
    # 删除购物车路由
    url(r'^delete/(\d+)/$', views.delete),
]

