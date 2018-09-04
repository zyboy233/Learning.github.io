from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello')
def justTest(request):
    myId = request.GET.get('id','0')
    name = request.GET.get('name','zhangsan')
    return HttpResponse('name=%s , id=%s' % (name,myId))
def second(request,mid,name):
    return HttpResponse('id=%s,name=%s' % (mid,name))

def third(request,a,b,name):
    c = int(a) + int(b)
    return HttpResponse('sum=%s,name=%s' % (c,name))