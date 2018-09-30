from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import RegistForm,LoginForm,EmailForm
from django.contrib.auth.hashers import make_password,check_password
from .models import MyUser,EmailRecord
from utils.my_email import sendEmail
# Create your views here.

class RegistView(View):
    def get(self,request):
        regist_form = RegistForm()
        return  render(request,'regist.html',{'regist_form':regist_form})
    def post(self,request):
        regist_form = RegistForm(request.POST)

        if regist_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = MyUser.objects.filter(email=email)
            if user:
                return render(request,'regist.html',{'msg':'该用户已经注册'})
            else:
                user = MyUser()
                user.email = email
                user.password = make_password(password)
                user.username = email
                user.is_active = 0
                user.save()
                email = sendEmail(email)
                return render(request,'tips.html')
        else:
            return render(request,'regist.html',{'regist_form':regist_form})
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = MyUser.objects.get(email=email)
            result = check_password(password,user.password)
            if result:
                if user.is_active == 0:
                    res = sendEmail(email,EmailRecord.objects.get(email=email).code)
                    return render(request,'login.html',{'msg':'账号未激活,请前往邮箱激活账号'})
                else:
                    return HttpResponseRedirect('/home/')
            else:
                return render(request,'login.html',{'msg':'账号或密码错误'})
        else:
            return render(request,'login.html',{'login_form':login_form})
def page(request):
    return render(request,'page.html')
def home(request):
    return render(request,'home.html')
class ActiveView(View):
    def get(self,request,code):
        try:
            record = EmailRecord.objects.get(code=code)
        except Exception as e:
            return render(request,'active_fail.html')
        else:
            user = MyUser.objects.get(email=record.email)
            user.is_active = 1
            user.save()

            return render(request,'login.html')
class ForgetView(View):
    def get(self,request):
        return render(request,'forget.html')
    def post(self,request):
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email = request.POST['email']
            res = sendEmail(email=email,email_type = 'forget')
            if res == 1:
                return render(request,'login.html',{'msg':'请到邮箱重置密码'})
            else:
                return render(request,'forget.html',{'msg':'未知错误,邮件发送失败'})
        else:
            return render(request,'forget.html',{'email_form':email_form})
class ResetView(View):
    def get(self,request,code):
        email = EmailRecord.objects.get(code=code).email

        return render(request,'reset.html')