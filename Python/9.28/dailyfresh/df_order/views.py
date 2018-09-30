# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from df_cart.models import CartInto
from df_goods.models import GoodsInfo
from df_user.models import UserInfo
from df_user.islogin import islogin
from .models import OrderInfo, OrderDetailInfo

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.
@islogin
def order(request):
    if request.method == "GET":
        userid = request.session.get('u_id')
        user = UserInfo.objects.get(id=userid)

        # 获取购物车页面勾选的所有商品，没有勾选的商品，form表单在进行submit提交的时候，是不会将input标签的value值提交的。
        # getlist：获取name="cartid"的input标签的value值。
        cartid_list = request.GET.getlist('cartid')

        cart_list = []
        # 根据购物车id，查询对应的商品
        for cartid in cartid_list:
            cart = CartInto.objects.get(id=cartid)
            cart_list.append(cart)
        context = {
            'title': '天天生鲜-订单页面',
            'type': 'goods',
            'is_detail': 0,
            'cart_list': cart_list,
            'user': user,
        }

        return render(request, 'df_order/place_order.html', context)

@islogin
def add_order(request):
    goods_list = request.POST.getlist('goods_list')
    total_price = request.POST['total_price']

    order = OrderInfo()
    order.user = UserInfo.objects.get(id=request.session.get('u_id'))
    order.o_id = '%s%s'%(datetime.now().strftime('%Y%m%d%H%M%S'),request.session.get('u_id'))
    order.o_date = datetime.now()
    order.o_total_price = total_price

    order.save()

    for goods_name in goods_list:
        goods = GoodsInfo.objects.get(g_title=goods_name)
        order_detail_info = OrderDetailInfo()
        order_detail_info.goods = goods
        order_detail_info.order = order

        # 订单信息和订单对应商品信息保存完毕，删除购物车
        cart = goods.cartinto_set.filter(goods_id=goods.id)[0]
        order_detail_info.count = cart.count

        order_detail_info.save()

        cart.delete()

    return JsonResponse({'result': 'success'})


