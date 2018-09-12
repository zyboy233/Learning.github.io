from django.shortcuts import render
from .models import Stu,Clsroom
from django.http import HttpResponse
# Create your views here.

def add(request):

    s1 = Stu(name='张三',age=18)
    s2 = Stu(name='李四',age=20)
    s1.save()
    s2.save()
    c1 = Clsroom(space='100平')
    c2 = Clsroom(space='200平')
    c2.save()
    c1.save()
    c1.code.add(s1,s2)
    c2.code.add(s1)
    return HttpResponse('添加成功')
def select(request):

    s1 = Stu.objects.get(name='张三')
    c_list = s1.clsroom_set.all()
    for c in c_list:
        print('----------')
        print(c.space)

    c1 = Clsroom.objects.get(space='100平')
    p_list = c1.code.all()
    for p in p_list:
        print('+++++++')
        print(p.name,p.age)
    return HttpResponse('查询成功')