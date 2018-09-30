# coding:utf-8
# __author__ = 'Gao'

"""
实现用户从哪一个页面跳转到登录页面的，那么登录之后就回到这个页面。
解决这个问题需要记录用户当前点击的是哪一个url，用户登录成功之后，再将这个url获取出来，再进行访问就可以了。
"""

from django.http import HttpResponseRedirect

def islogin(func):
    def login_function(request, *args, **kwargs):
        if request.session.get('u_name'):
            # 说明用户已经登录了，直接访问用户点击的那个连接即可。
            return func(request, *args, **kwargs)
        else:
            # 说明用户没有登录，跳转到登录页面，同时将用户访问的当前的Url记录下来。
            response = HttpResponseRedirect('/user/login/')
            response.set_cookie('url', request.get_full_path())
            return response
    return login_function


