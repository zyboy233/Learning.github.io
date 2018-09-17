from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import RegistForm
from .models import MyUser

# Create your views here.

class Register(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):

        username = request.POST['username']
        password = request.POST['password']

        regist_form = RegistForm(request.POST)
        if regist_form.is_valid():
            if MyUser.objects.filter(username=username):
                return HttpResponse('用户已存在')
            else:
                MyUser.objects.create(username=username,password=password)
                return HttpResponse('注册成功')
        else:
            return HttpResponse('用户名或密码不合法')


