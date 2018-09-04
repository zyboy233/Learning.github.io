from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def secondPage(request):
    # return HttpResponse('哈哈哈哈')
    context = {}
    context['hello'] = 'hello world'
    return render(request,'second.html',context)