from django.shortcuts import render
from django.http import HttpResponse
from .models import People,Card
# Create your views here.
def add(request):
    p1 = People(name='张三',age=18,code='101')
    p2 = People(name='李四',age=20,code='102')
    p1.save()
    p2.save()
    c1 = Card(card_code=p1,card_type='gold')
    c2 = Card(card_code=p2,card_type='black')
    c1.save()
    c2.save()
    return HttpResponse('添加成功')
def select(request):
    p = People.objects.get(name='张三')
    print('+++++++++++++')
    print(p.card.card_type)

    c = Card.objects.get(card_type='black')
    p = c.card_code
    print('-------',p)
    return HttpResponse('查询成功')