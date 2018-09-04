from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import First

def home(requset):
    allData = First.objects.all()

    objects = list()
    for data in allData:
        objects.append('姓名:'+data.name + ',描述:' +data.des)
    response_html = '<br>'.join(objects)
    return HttpResponse(response_html)