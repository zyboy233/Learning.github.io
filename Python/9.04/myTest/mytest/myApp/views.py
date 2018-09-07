from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Table1
# Create your views here.

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
def home(request):
    p = Person('张三',18)
    content = {
        'person':p
    }
    return render(request,'index.html',content)
def form_search(request):
    return render_to_response('search_form.html')
def search(request):
    request.encoding = 'utf-8'
    print(request.GET,'------')
    if 'q' in request.GET:
        message = '你搜索的内容为:' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
def add_user(request):
    return render(request,'add_user.html')
def receive_user(request):
    request.encoding = 'utf-8'
    if 'q'and 'p' in request.GET:
        if Table1.objects.create(name=request.GET['q'] , age=request.GET['p']):
            message = ('添加用户成功:',request.GET['q']+ ',' +request.GET['p'])
        else:
            message = ('添加失败')
    else:
        message = ('未接收到数据')
    content = {
        'message':message
    }
    return render(request,'add_user.html',content)
def receive_user_post(request):
    ctx = {}
    if 'q' in request.POST:
        ctx['rlt'] = request.POST['q'] + ','+ request.POST['p']
    return render(request,'add_user_post.html',ctx)


