from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def regist(request):
    return HttpResponse('myFirst里面的注册页面')
def login(request):
    return HttpResponse('myFirst里面的登录页面')
