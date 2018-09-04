from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myFirst(request):
    return HttpResponse('网址3,第一个页面')
def mySecond(request):
    return HttpResponse('网址3,第二个页面')