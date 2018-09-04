from django.conf.urls import url
from . import views

urlpatterns = [
    # 注意 url和path的区别
    # http://localhost:8000/index/justtest/?id=100&name=lisi
    url('justtest/',views.justTest),
    url(r'second/(\d+)/(\w+)',views.second),

    # ?P<a> 赋值
    # http://localhost:8000/index/third/1000/2000/hello
    url(r'third/(?P<a>\d+)/(?P<b>\d+)/(?P<name>\w+)',views.third)
]