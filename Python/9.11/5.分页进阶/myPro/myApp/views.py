from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import random
from .models import Goods
# Create your views here.
def index(request):
    # for x in range(200):
    #     good = Goods(name='good%s' % x,des='该商品物美价廉,只需{}元'.format(random.randint(10,100)))
    #     good.save()
    return HttpResponse('数据添加成功')
def select(request):
    good_list = Goods.objects.all()

    # 值3:当最后一页数据少于n条 将数据并入上一页
    paginator = Paginator(good_list,12,3)

    try:
        # GET请求方式 get()获取指定Key值所对应的Value值
        # 获取index的值 如果没有 则色湖之使用默认值1
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        # 如果输入的页码数不是整数 那么显示第一页数据
        number = paginator.page(1)

    except EmptyPage :
        # 如果获取的页码数不再当前页码范围内 则显示最后一页
        # paginator.num_pages 获取当前总页数
        # paginator.page() 获取指定的某一页
        number = paginator.page(paginator.num_pages)

    # 将当前页页码 以及当前页数据传到index.html

    return render(request,'index.html',{'page':number,'paginator':paginator})

