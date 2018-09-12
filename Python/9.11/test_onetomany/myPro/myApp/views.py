from django.shortcuts import render
from django.http import HttpResponse
from .models import People,Games
# Create your views here.

def add(request):
    p1 = People(name='张三',age='18')
    p2 = People(name='李四',age='20')
    p1.save()
    p2.save()

    g1 = Games(gname='pgub',gtype='fps',bind=p1)
    g2 = Games(gname='dota',gtype='moba',bind=p1)
    g3 = Games(gname='csgo',gtype='fps',bind=p2)
    g4 = Games(gname='cod',gtype='单机',bind=p2)

    g1.save()
    g2.save()
    g3.save()
    g4.save()

    return HttpResponse('添加成功')
def select(request):

    p = People.objects.get(name='张三')
    g_list = p.games_set.all()
    for g in g_list:
        print('----------------------')
        print(g.gname,g.gtype,g.bind_id)

    g = Games.objects.get(gname = 'csgo')
    print(g.bind.name)

    g_list = p.games_set.all()
    for g in g_list:
        print('+++++++++++++++')
        print(g.gname,g.gtype)
    return HttpResponse('查询成功')