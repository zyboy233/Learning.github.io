from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def index(request):
    p = People('小明',99)
    newTime = datetime.datetime.now()
    content = {
        'name':'张三',
        'font_list':['吃饭','睡觉','玩手机','看视频','扯淡'],
        'friend':p,
        'study_list':['c','HTML','JS','Python','Node','UI'],
        'today':newTime,
        'girl_friend':{
            'name':'小美',
            'height':'160',
            'hasKuang':True
        }
    }

    # return render(request,'index.html',content)
    # render渲染html文件的时候  会从项目当中的templates里面找
    # 所以无需设置templates路径  如果app的templates里面有和
    # 项目的templates里的文件重名的时候  只需在里面新建一个文件夹
    # 然后将重名的文件放入其中  渲染文件时跟上新建的文件夹路径即可
    return render(request,'templ/index.html',content)
