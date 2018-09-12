from django.shortcuts import render
from django.http import HttpResponse
from .models import People,Card
# Create your views here.
def add(request):
    # p1 = People.objects.create(name='小王',car_num = 4)
    # p2 = People.objects.create(name='老王',car_num = 40)
    #
    # c1 = Card(number='101',source='中国银行',person=p1)
    # c2 = Card(number='102',source='中国农行',person=p1)
    # c3 = Card(number='110',source='中国建行',person=p1)
    # c1.save()
    # c2.save()
    # c3.save()
    # c4 = Card(number='201',source='郑州美容美发',person=p2)
    # c5 = Card(number='202',source='郑州交通一卡通',person=p2)
    # c6 = Card(number='203',source='郑州逍遥镇胡辣汤',person=p2)
    # c7 = Card(number='204',source='郑州惠济四附院',person=p2)
    # c4.save()
    # c5.save()
    # c6.save()
    # c7.save()
    return HttpResponse('添加成功')
def select(request):
    c1 = Card.objects.get(number='203')
    print(c1.person.name)

    c2 = Card.objects.get(id=3)
    print(c2.person.name)

    # 类__字段
    # 类_set
    result = c2.person.card_set.all()
    print(result)
    for res in result:
        print(res.source)

    result = People.objects.get(name='老王')
    for card in result.card_set.all():
        print(card.source)

    return HttpResponse('查询成功')