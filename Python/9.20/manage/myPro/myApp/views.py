from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import RegisterForm,LoginForm,ForgetForm,ResetForm,InfoForm
from .models import UserProfile,EmailRecord,ResetWithEmail,Subject
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import auth
from utils.email_send import send_email
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')
def regist(request):
    return render(request,'register.html')

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = UserProfile.objects.filter(email=email)
            if user:
                return render(request,'register.html',{'register_form':register_form,'msg':'该用户已经被注册'})
            user = UserProfile()
            user.username = email
            user.email = email
            user.is_active = 0
            # make 制作
            # make_password 将之前的密码进行加密
            user.password = make_password(password)
            user.save()
            # 注册成功的同时 发送邮件给对方 通知对方注册成功
            email = send_email(email)
            return render(request,'tips.html',{'title':'注册成功','url':'/login/login/'})
        else:
            return render(request,'register.html',{'register_form':register_form})

class LoginView(View):
    def get(self,request):

        return render(request,'login.html')
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            # user = UserProfile.objects.filter(email=email)
            # 验证账号密码是否一致
            # user = authenticate(email=email,password=password)
            user = UserProfile.objects.get(email=email)
            result = check_password(password,user.password)
            print(result,'----------------')
            if result:
                if user.is_active == 1:
                    user.save()
                    response = HttpResponseRedirect('/subject/')
                    response.set_cookie('username',email,3600)
                    return response
                else:
                    code_obj = EmailRecord.objects.get(email=email)
                    code = code_obj.code
                    send_email(email=email)
                    return render(request,'login.html',{'login_form':login_form,'msg':'该账号尚未被激活,请前往邮箱激活!'})
            else:
                return render(request,'login.html',{'login_form':login_form,'msg':'账号密码不匹配,请核对!'})
        else:
            return render(request,'login.html',{'login_form':login_form})

class ActiveView(View):
    def get(self,request,code):
        try:
            # 根据指定的激活码找对应的邮箱
            email_code = EmailRecord.objects.get(code=code)
        except Exception as e :
            # 如果邮箱没有找到
            return render(request,'active_fail.html')
        else:
            # 如果邮箱被找到
            user = UserProfile.objects.get(email=email_code.email)
            user.is_active = 1
            user.save()
            return render(request,'login.html')
    def post(self,request,code):
        pass

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        pass

class ForgetView(View):
    def get(self,request):
        return render(request,'forget.html')
    def post(self,request):
        email_obj = ForgetForm(request.POST)
        if email_obj.is_valid():
            email = request.POST['email']
            result = send_email(email,email_type='forget')
            if result == 1:
                # 确保数据库智游一条数据
                reset_email = ResetWithEmail.objects.filter(id=1)
                if reset_email:
                    reset_email[0].email = email
                    reset_email[0].save()
                else:
                    reset_email = ResetWithEmail()
                    reset_email.email = email
                    reset_email.save()
                return render(request,'login.html',{'title':'邮件发送成功','url':'/login/login/','msg':'前往邮箱重置密码'})
            else:
                return render(request, 'forget.html',{'msg':'未知错误,邮件发送失败'})
        else:
            return render(request,'forget.html',{'form':email_obj})

class ResetView(View):
    def get(self,request,reset):
        print(reset,'++++++++++++++++++++++++++')
        return render(request,'reset.html')
    def post(self,request,reset):
        return render(request,'reset.html')

class ResetPage(View):
    def get(self,request):
        return render(request,'reset.html')
    def post(self,request):
        reset_obj = ResetForm(request.POST)
        if reset_obj.is_valid():
            password = request.POST['password']
            again = request.POST['again']
            if password == again:
                email = ResetWithEmail.objects.get(id=1)
                user = UserProfile.objects.get(email=email.email)
                user.password = make_password(password)
                user.save()
                return render(request,'login.html')
            else:
                return render(request,'reset.html',{'msg':'两次密码不一致'})
        else:
            return render(request,'reset.html',{'reset_form':reset_obj})

class SubjectView(View):
    def get(self,request):
        username = request.COOKIES.get('username', '')
        print(username,'++++++++++')
        if not username:
            return render(request,'login.html')
        try:
            subname = request.GET['sub']
            print(subname, '-------------')
        except Exception as e:
            subjects = Subject.objects.all()
            return render(request, 'subject.html', {'subjects': subjects,'username':username})
        else:
            subject = Subject.objects.get(name=subname)
            return render(request, 'info.html', {'subject': subject,'username':username})

class EditView(View):
    def get(self,request):
        username = request.COOKIES.get('username', '')
        if not username:
            return render(request, 'login.html')
        subname = request.GET['sub']
        subject = Subject.objects.get(name=subname)
        return render(request,'edit.html',{'subject':subject,'username':username})
    def post(self,request):
        username = request.COOKIES.get('username', '')
        if not username:
            return render(request, 'login.html')
        subjects = Subject.objects.all()
        oldname = request.POST['oldname']

        subject = Subject.objects.get(name=oldname)
        subject.name = request.POST['name']
        subject.amount = request.POST['amount']
        subject.days = request.POST['days']
        subject.number = request.POST['number']
        subject.assurance = request.POST['assurance']
        subject.remark = request.POST['remark']
        sub_form = InfoForm(request.POST)
        if sub_form.is_valid():
            if request.POST['oldname']==request.POST['name'] or len(Subject.objects.filter(name=request.POST['name']))==0:
                subject.save()
                subjects = Subject.objects.all()
                return render(request,'subject.html',{'subjects':subjects,'msg':'修改成功','username':username})
            else:
                return render(request, 'subject.html', {'subjects': subjects, 'msg': '该学科已存在,修改失败','username':username})
        else:
            return render(request, 'subject.html', {'subjects': subjects, 'sub_form':sub_form,'username':username})

class AddView(View):
    def get(self,request):
        username = request.COOKIES.get('username', '')
        print(username, '++++++++++')
        if not username:
            return render(request, 'login.html',{'username':username})
        return render(request,'add.html')
    def post(self,request):
        username = request.COOKIES.get('username', '')
        print(username, '++++++++++')
        if not username:
            return render(request, 'login.html')
        subjects = Subject.objects.all()
        sub_form = InfoForm(request.POST)
        if sub_form.is_valid():
            subject = Subject()
            subject.name = request.POST['name']
            subject.amount = request.POST['amount']
            subject.days = request.POST['days']
            subject.number = request.POST['number']
            subject.assurance = request.POST['assurance']
            subject.remark = request.POST['remark']
            if not Subject.objects.filter(name=request.POST['name']):
                subject.save()
                subjects = Subject.objects.all()
                return render(request,'subject.html',{'subjects':subjects,'msg':'添加成功','username':username})
            else:
                return render(request,'subject.html',{'subjects':subjects,'msg':'该学科已存在,添加失败','username':username})
        else:
            print(sub_form,'+++++++++++++++++++')
            return render(request, 'subject.html', {'subjects': subjects, 'sub_form':sub_form})

class DeleteView(View):
    def get(self,request):
        username = request.COOKIES.get('username', '')
        print(username, '++++++++++')
        if not username:
            return render(request, 'login.html')
        subname = request.GET['sub']
        subject = Subject.objects.get(name=subname).delete()

        subjects = Subject.objects.all()
        return render(request,'subject.html',{'msg':'删除成功!','subjects':subjects,'username':username})

class LogoutView(View):
    def get(self,request):
        response = HttpResponseRedirect('/subject/')
        # 清除cookie里保存的username
        response.delete_cookie('username')
        return response

"""
使用验证码时候的问题
1.RuntimeError: Model class captcha.models.CaptchaStore doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
 在setttings里面进行注册app
2.Make sure you've included captcha.urls as explained in the INSTALLATION section on http://readthedocs.org/docs/django-simple-captcha/en/latest/usage.html#installation
 在项目里面urls进行设置
3.no such table
  重新模型迁移
"""