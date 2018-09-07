from django.shortcuts import render
from django.http import HttpResponse
from myApp.my_form import AddForm
# Create your views here.

def index(request):
    content = {
        'title':'index',
        'my_friends':['张三','李四','王五','赵六'],
        'my_girl_friend':{
            'name':'小红',
            'age':'20',
            'has_kuang':True
        }
    }

    # return render(request,'index.html')
    return render(request,'myapp_index.html',content)
    # return render(request,'temp/index.html')

def home(request):
    form = AddForm()
    return render(request,'home.html',{'form':form})

def add(request):
    return HttpResponse('hhhhhhhhh')