from django.shortcuts import render
from .models import Person
from django.http import HttpResponse
# Create your views here.

def index(request):
    # 方法1:
    # first = Person(uname='张三',uage=17,usex=True)
    # first.save()


    #  方法2:
    # first = Person.objects.create(uname='李四',uage=18,usex=True)

    # 方法3:
    # first = Person()
    # first.uname = '小美'
    # first.uage = 20
    # first.usex = False
    # first.save()

    # 方法4:
    # Person.objects.get_or__create(uname='王五',uage=21,usex=True)

    # 查询
    all = Person.objects.all()

    # 找到的结果是一个容器 里面可能有多个值
    # 也可能没有值
    # 如果没有值 程序也不会报错
    first = Person.objects.filter(uname='小美')[0]
    # 修改值
    first.uname = '太美'
    first.save()
    # 删除值
    Person.objects.filter(uname='李四')[0].delete()
    return render(request,'index.html',{'all':all,'find':first})

