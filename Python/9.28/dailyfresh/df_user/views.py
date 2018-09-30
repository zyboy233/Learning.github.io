# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hashlib import sha1
from df_user.models import UserInfo
from df_user.islogin import islogin
from df_goods.models import GoodsInfo
from df_order.models import OrderInfo, OrderDetailInfo

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
# 注册视图函数
def register(request):
    if request.method == "GET":
        return render(request, 'df_user/register.html',{'title':'天天生鲜-注册'})
    else:
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        email = request.POST.get('email')

        # 保存用户之前，对密码进行加密
        s = sha1()
        s.update(pwd)
        # 相同字符串加密结果是一样的
        sha1_pwd = s.hexdigest()

        user = UserInfo()
        user.u_name = username
        user.u_password = sha1_pwd
        user.u_email = email
        user.save()

    # 注册成功，重定向登录页面
    return redirect('/user/login/')


def checkuser(request):
    username = request.GET.get('username')
    user = UserInfo.objects.filter(u_name=username)
    if user:
        return JsonResponse({'result':'exist'})
    else:
        return JsonResponse({'result':'noexist'})

def login(request):
    if request.method == "GET":
        return render(request, 'df_user/login.html', {'title': '天天生鲜-登录', 'error_username': 0, 'error_pwd':0})
    else:
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        jizhu = request.POST.get('jizhu')
        # 查询用户名是否存在
        user = UserInfo.objects.filter(u_name=username)
        if user:
            s = sha1()
            s.update(password)
            if s.hexdigest() == user[0].u_password:
                url = request.COOKIES.get('url', '')
                if url == '':
                    response_redirect = HttpResponseRedirect('/user/info/')
                else:
                    response_redirect = HttpResponseRedirect(url)
                # 用户名和密码都正确
                if jizhu != 0:
                    response_redirect.set_cookie('u_name', username)
                else:
                    response_redirect.set_cookie('u_name', '')
                # 将用户名同时存储到session中，来表明用户的登录状态
                request.session['u_name'] = username
                request.session['u_id'] = user[0].id
                return response_redirect
            else:
                # 用户名正确，密码错误
                context = {
                    'title': '天天生鲜-登录',
                    'username': username,
                    'password': password,
                    'error_pwd': 1,
                    'error_username': 0,
                }
                return render(request, 'df_user/login.html', context)
        else:
            # 用户名错误
            context = {
                'title': '天天生鲜-登录',
                'username': username,
                'password': password,
                'error_pwd': 0,
                'error_username': 1,
            }
            return render(request, 'df_user/login.html', context)

@islogin
def info(request):
    user = UserInfo.objects.get(id=request.session['u_id'])
    # 需要从cookie中读取浏览商品的id，将这些商品信息展示在用户中心的 “最近浏览” 中。
    goods_id = request.COOKIES.get('goods_id','')
    if goods_id != '':
        # 有浏览详情记录
        goods_id_list = goods_id.split(';')
        goods_list = []
        for id in goods_id_list:
            # 根据id查商品
            goods = GoodsInfo.objects.get(id=int(id))
            goods_list.append(goods)
        context = {
            'title': '天天生鲜-用户中心',
            'type': 'user',
            'info': 1,
            'user': user,
            'goods_list': goods_list
        }
    else:
        context = {
            'title': '天天生鲜-用户中心',
            'type': 'user',
            'info': 1,
            'user': user,
        }
    return render(request, 'df_user/user_center_info.html', context)

@islogin
def order(request):
    context = {
        'title': '天天生鲜-用户中心',
        'type': 'user',
        'order': 1,
    }
    return render(request, 'df_user/user_center_order.html', context)

@islogin
def detail_order(requets, page_num):
    # 查询当前登录用户的所有订单信息
    orderinfo = OrderInfo.objects.filter(user_id=requets.session.get('u_id'))
    # 每一页展示2个订单
    paginator = Paginator(orderinfo, 2)
    page = paginator.page(page_num)
    context = {
        'title': '天天生鲜-全部订单',
        'info': 'user',
        'page': page,
        'page_num': page_num,
        'order': 1,
        'type': 'user',
    }
    return render(requets, 'df_user/user_center_order.html', context)

@islogin
def site(request):
    # 获取当前登录用户
    user = UserInfo.objects.get(id=request.session['u_id'])
    if request.method == "POST":
        user.u_shou_address = request.POST.get('address')
        user.u_phone = request.POST.get('phone')
        user.u_postcode = request.POST.get('postcode')
        user.save()
    context = {
        'title': '天天生鲜-用户中心',
        'type': 'user',
        'site': 1,
        'user': user,
    }
    return render(request, 'df_user/user_center_site.html', context)

def mylogout(request):
    del request.session['u_name']
    return render(request, 'df_goods/index.html')
