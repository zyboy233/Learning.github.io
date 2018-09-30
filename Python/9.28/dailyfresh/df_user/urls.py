# coding:utf-8
# __author__ = 'Gao'

from django.conf.urls import url
from . import views
urlpatterns = [
    # 注册路由
    url(r'^register/$', views.register),
    # 检查用户名是否已被占用的路由
    url(r'^checkuser/$', views.checkuser),
    # 登录路由
    url(r'^login/$', views.login),
    # 用户个人中心路由
    url(r'^info/$', views.info),
    # 全部订单/收货地址
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
    url(r'^logout/$', views.mylogout),
    url(r'^order/(?P<page_num>\d+)/$', views.detail_order),
]
