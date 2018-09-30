# coding:utf-8
# __author__ = 'Gao'

from haystack.views import SearchView
from .models import *


class MySeachView(SearchView):
    def extra_context(self):  # 重载extra_context来添加额外的context内容
        context = super(MySeachView, self).extra_context()
        side_list = GoodsInfo.objects.filter(g_type_id='1').order_by('-id')[:2]
        context['title'] = '搜索结果'
        context['newsgoods'] = side_list
        return context

