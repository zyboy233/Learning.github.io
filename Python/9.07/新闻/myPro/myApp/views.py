from django.shortcuts import render
import requests
from .models import Data
# Create your views here.
def index(request):
    url = 'https://www.apiopen.top/journalismApi'

    data_json = requests.get(url).json()

    for type_list in data_json['data'].values():
        for article in type_list:
            sourse = article['source']
            title = article['title']
            link = article['link']
            category = article['category']
            ptime = article['ptime']
            Data.objects.create(sourse=sourse,title=title,link=link,category=category,ptime=ptime)
    return render(request,'index.html',{'status':'success'})
