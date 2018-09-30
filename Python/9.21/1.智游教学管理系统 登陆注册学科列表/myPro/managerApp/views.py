import json
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from .models import UserModel
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate
# 验证登陆的装饰器
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegisterView(View):
    """注册"""
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        if len(username) == 0 or len(password) == 0:
            return render(request,'register.html',{'msg':'账号和密码不能为空'})
        if UserModel.objects.filter(username=username):
            return render(request,'register.html',{'msg':'该用户已经注册'})
        user = UserModel()
        user.username = username
        # 密码加密存储
        password = make_password(password)
        print(password)
        user.password = password
        user.save()

        return render(request,'login.html',{'msg':'注册成功,请登录'})
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        # 获取user对象
        user = UserModel.objects.get(username=username)
        # 取值成功返回user对象,不成功返回None
        user = authenticate(username=username,password=password)
        # 验证密码
        bool_value = check_password(password,user.password)
        # if UserModel.objects.filter(username=username,password=password):
        #     user = UserModel.objects.get(username=username)
        if user:
            # 获取当前登陆的对象,request.user
            login(request,user)
            return redirect('/subject/')
        else:
            return render(request,'login.html',{'msg':'账号或者密码错误'})

class LoginOutView(View):
    """注销"""
    def get(self,request):
        # 清除登陆信息,从request对象中删除user对象
        logout(request)
        return redirect('/user/login/')

# 函数视图
# status_code 状态码
# 4开头 客户端报错
# 5开头 服务器内部错误
# 2开头 成功
# 3开头 跳转和转移
@login_required
def  test_json(request):
    if request.method == "POST":
        json_id=request.POST['json_id']
        a = request.POST['a']
        b = request.POST['b']
        print(a,b,json_id)
    return HttpResponse(json.dumps({'a':'ok'}),content_type='application/json')
def page_not_found(request):
    return render(request,"404.html",status=404)
def page_error(request):
    return render(request,"404.html",status=500)