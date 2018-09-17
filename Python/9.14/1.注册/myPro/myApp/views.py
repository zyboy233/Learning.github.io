from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from .models import CustomUser
from django.http import JsonResponse
# Create your views here.

class Register(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        # 获取请求对象里面的所有参数值
        # 使用RegisterForm是为了更方便的验证账号密码格式是否正确
        # 因为RegisterForm里面的每一个字段都设置了限制条件
        regist_form = RegisterForm(request.POST)
        # 如果格式正确
        # json格式
        result = {}
        if regist_form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            # filter 过滤 email1 字段 email2 值
            if CustomUser.objects.filter(email=email):
                result['code'] = 101
                result['message'] = '该用户已注册'
            else:
                user = CustomUser()
                user.username = email
                user.email = email
                user.password = password
                user.save()
                result['code'] = 200
                result['message'] = '恭喜注册成功'
            return JsonResponse(result)
        else:
            result['code'] = 301
            result['message'] = '账号密码格式不正确'
            return JsonResponse(result)