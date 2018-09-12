from django.shortcuts import render
from .models import One,Two

# Create your views here.

def index(request):
    o1 = One.objects.create(oname='张三1',oage='11',odate='2011-11-11')
    o2 = One.objects.create(oname='张三2',oage='12',odate='2012-12-12')

    t1 = Two.objects.create(tsub=o1,tfond='o1',tdes='我喜欢o1')
    t2 = Two.objects.create(tsub=o2,tfond='o2',tdes='我喜欢o2')
    return render(request,'index.html')
def select(request):
    # 查询关联表中的数据
    # t1 = Two.objects.get(tfond='o1')
    # o1 = t1.tsub

    t1 = Two.objects.get(tsub__oname='张三1')

    return render(request,'index.html',{'t1':t1})