from django.shortcuts import render
from django.http import HttpResponse
from .models import People,Card
# Create your views here.

def add(request):

    p1 = People(name='张三',age=18)
    p2 = People(name='李四',age=19)
    p3 = People(name='王五',age=20)

    p1.save()
    p2.save()
    p3.save()

    c1 = Card(code='111111',address='c1的家',person=p1)
    c2 = Card(code='222222',address='c2的家',person=p2)
    c3 = Card(code='333333',address='c3的家',person=p3)

    c1.save()
    c2.save()
    c3.save()
    return HttpResponse('添加成功')
def select(request):
    p = People.objects.get(name='张三')

    print(p.name,p.age,p.card.code,p.card.address)

    c = Card.objects.get(person__name='张三')

    print(c.person.name,c.person.age,c.code,c.address)


    p = People.objects.get(card__code = '222222')
    print(p.name,p.age,p.card.code,p.card.address)
    return HttpResponse('查找成功')