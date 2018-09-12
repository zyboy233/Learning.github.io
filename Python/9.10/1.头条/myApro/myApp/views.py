from django.shortcuts import render
import requests
from .models import TouTiaoNews
# Create your views here.

def index(request):
    url = 'https://www.apiopen.top/journalismApi'

    data_dic = requests.get(url).json()

    all_news_list = []
    for item in data_dic['data'].values():
        for news in item:
            tou_tiao = TouTiaoNews()
            tou_tiao.title = news['title']
            tou_tiao.link = news['link']
            tou_tiao.source = news['source']
            tou_tiao.time = news['ptime']
            tou_tiao.save()
            all_news_list.append(tou_tiao)

    return render(request,'index.html',{'allNews':all_news_list})