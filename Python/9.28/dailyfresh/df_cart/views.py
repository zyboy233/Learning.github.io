# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from df_user.islogin import islogin
from df_user.models import UserInfo
from df_goods.models import GoodsInfo
from .models import CartInto

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse

# Create your views here.

@islogin
def cart(request):
    user = UserInfo.objects.get(u_name=request.session['u_name'])
    # 根据用户id查询该用户购买的所有商品
    all_cart = CartInto.objects.filter(user_id=user.id)
    if len(all_cart) == 0:
        all_cart = ''
    context = {
        'title': '天天生鲜-购物车',
        'type': 'cart',
        'all_cart': all_cart
    }
    return render(request, 'df_cart/cart.html', context)

@islogin
def add(request, goodsid, count):
    # 将商品的id，商品数量，用户的id保存成购物车的一条数据记录。
    user_id = request.session.get('u_id')
    goods_id = int(goodsid)
    count = int(count)
    # 在保存数据之前，先去购物车表中，查看当前用户user_id购买的商品goods_id是否已经存在，已经存在的话，不需要再添加一条记录，只需修改购买数量即可。
    cart_list = CartInto.objects.filter(user_id=user_id, goods_id=goods_id)
    if len(cart_list) == 0:
        # 购物车没有记录
        cart = CartInto()
        cart.user_id = user_id
        cart.goods_id = goods_id
        cart.count = count
    else:
        # 已经存在记录
        cart = cart_list[0]
        cart.count = cart.count + count
    cart.save()

    # 查询当前用户所有购物车的商品，统计总的商品数量
    cart_list = CartInto.objects.filter(user_id=user_id)
    total_count = 0
    for cart in cart_list:
        total_count += cart.count

    return JsonResponse({'count': total_count})

@islogin
def update(request, cartid, count):
    cart = CartInto.objects.get(id=cartid)
    cart.count = int(count)
    cart.save()
    return JsonResponse({'success': 1})


@islogin
def delete(request, cartid):
    cart = CartInto.objects.get(id=int(cartid))
    cart.delete()
    return JsonResponse({'success': 1})
