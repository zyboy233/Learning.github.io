from django.urls import path
from django.conf.urls import url

from goods.views import index,list,detail,MySearchView,comment,add_comment
from user.views import handle_wx

app_name = 'goods'

urlpatterns = [
    path('',handle_wx),
    path('index/',index,name='index'),
    path('list/<int:category_id>/<str:sort>/<int:page_num>/',list,name='list'),
    # 商品的详情页
    path('detail/<int:goods_id>/',detail,name='detail'),
    # 评论
    path('comment/<int:goods_id>/',comment,name = 'comment'),
    # 添加评论
    path('add_comment/',add_comment,name='add_comment')
]