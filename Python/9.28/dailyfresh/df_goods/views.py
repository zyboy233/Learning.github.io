# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import TypeInfo, GoodsInfo
from df_cart.models import CartInto

from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # 首页中展示两块内容：商品列表4个商品，人气较高的3个商品
    # 对所有水果按照id进行降序排列。
    fruit = GoodsInfo.objects.filter(g_type_id=1).order_by('-id')[0:4]
    hot_fruit = GoodsInfo.objects.filter(g_type_id=1).order_by('-g_click')[0:3]

    # 查询当前用户所有购物车的商品，统计总的商品数量
    cart_list = CartInto.objects.filter(user_id=request.session['u_id'])
    total_count = 0
    for cart in cart_list:
        total_count += cart.count

    context = {
        'title': '天天生鲜-商品首页',
        'fruit': fruit,
        'hot_fruit': hot_fruit,
        'type': 'goods',
        'count': total_count,
    }

    return render(request, 'df_goods/index.html', context)

def goodslist(request, typeid, page_num, sort_type):
    """
    商品详情
    :param request:
    :param typeid: 商品所属分类id
    :param page_num: 分页中商品页码
    :param sort_type: 排序方式(default/price/hot)
    :return:
    """
    # 新品推荐
    newsgoods = GoodsInfo.objects.filter(g_type_id=typeid).order_by('-id')[0:2]
    # 商品列表部分
    if sort_type == 'default':
        # 默认排序
        allgoods = GoodsInfo.objects.all().order_by('-id')
    elif sort_type == 'price':
        # 价格排序
        allgoods = GoodsInfo.objects.all().order_by('g_price')
    elif sort_type == 'hot':
        # 价格排序
        allgoods = GoodsInfo.objects.all().order_by('-g_click')

    # 根据allgoods进行分页
    paginator = Paginator(allgoods, 2)
    page_obj = paginator.page(int(page_num))

    type = TypeInfo.objects.get(id=typeid)

    # 查询当前用户所有购物车的商品，统计总的商品数量
    cart_list = CartInto.objects.filter(user_id=request.session['u_id'])
    total_count = 0
    for cart in cart_list:
        total_count += cart.count

    context = {
        'title': '天天生鲜-商品列表',
        'type': 'goods',
        'is_detail': 0,
        'page': page_obj,
        'typeinfo': type,
        'newsgoods': newsgoods,
        'sort_type': sort_type,
        'page_num': int(page_num),
        'count': total_count,
    }
    return render(request, 'df_goods/list.html', context)

def detail(request, id):
    # 根据id查商品
    goods = GoodsInfo.objects.get(id=id)
    # 商品的浏览次数+1
    goods.g_click += 1
    goods.save()

    # 查商品类型
    typeinfo = TypeInfo.objects.get(id=goods.g_type_id)
    # 当前商品所属分类中最近加入的商品作为新品推荐
    newsgoods = goods.g_type.goodsinfo_set.order_by('-id')[0:2]
    # 查询当前用户所有购物车的商品，统计总的商品数量
    cart_list = CartInto.objects.filter(user_id=request.session['u_id'])
    total_count = 0
    for cart in cart_list:
        total_count += cart.count
    context = {
        'title': '天天生鲜-商品详情',
        'type': 'goods',
        'is_detail': 1,
        'goods': goods,
        'typeinfo': typeinfo,
        'newsgoods': newsgoods,
        'count': total_count,
    }
    # 当用户点进商品详情页面，将这个商品的id保存到cookie中，而且只需要保存5个，然后当用户进入个人信息页面时，就可以根据cookie中保存的5个商品的id并取出5个商品对象。
    response = render(request, 'df_goods/detail.html', context)
    goods_id = request.COOKIES.get('goods_id', '')
    if goods_id != '':
        # 不是第一次浏览商品详情
        # 按照;分割cookie字符串
        goods_id_list = goods_id.split(';')
        # 在保存其它的id之前，先判断这个id是否在cookie中已经保存过，保存过就不再保存，一个商品不管该用户浏览多少次，cookie中只记录一次。
        # goods_id_list: ['1', '2']
        if id not in goods_id_list:
            goods_id_list.insert(0, id)
        # 判断goods_id_list中的id数量是否超出5个，如果超出，把排在后面的id删除即可。
        if len(goods_id_list) >= 6:
            del goods_id_list[5]
        # 最终，将这个列表，转化为一个字符串，存入cookie
        goods_id = ';'.join(goods_id_list)
    else:
        # 是第一次浏览商品详情
        goods_id = id
    response.set_cookie('goods_id', goods_id)
    return response

