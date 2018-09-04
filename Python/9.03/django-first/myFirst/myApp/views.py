from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firstPage(request):
    # 注意 此处需要接受一个请求对象 并且返回一个响应对象
    # return HttpResponse('hello world')
    return render(request,'first.html')