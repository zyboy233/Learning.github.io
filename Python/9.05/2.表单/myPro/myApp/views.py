from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    form = forms.SumForm()
    return render(request,'index.html',{'form':form})
def add_form(request):
    if request.method == 'get':
        # get方法获取表单的值  可以通过GET['XX']方式
        # IntegerField() 只接受数字类型  这种类型才是合法的
        firstValue = request.GET['a1']
        secondValue = request.GET['b1']
        return HttpResponse(int(firstValue) + int(secondValue))
    else:
        # firstValue = request.POST['a1']
        # secondValue = request.POST['b1']
        # return HttpResponse(firstValue+secondValue)

        # 初始化一个请求对象 并且获取请求表达式和请求内容
        form = forms.SumForm(request.POST)
        # valid 合法;可用
        if form.is_valid():
            firstValue = form.cleaned_data['a1']
            secondValue = form.cleaned_data['b1']
            return HttpResponse(int(firstValue) + int(secondValue))
        else:
            return HttpResponse(request,'index.html')