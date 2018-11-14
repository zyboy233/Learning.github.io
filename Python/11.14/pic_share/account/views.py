from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from account.forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from account.models import Profile

def user_lgoin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                password=cd['password'])
            if user is None:
                return HttpResponse('登陆失败')
            else:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('登陆验证成功')
                else:
                    return HttpResponse('您的用户被禁用,请联系管理员解封')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form': form})

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'selection':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # 建立新数据对象,但是不写入数据库
            new_user = user_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_form.cleaned_data['password'])
            # 保存user对象
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})

@login_required()
def edit(request):
    if request.method == 'POST':
        print(request.POST)
        # instance 指定对象是数据库中的当前登陆用户的哪一行数据对象,如果不指定将新建记录而不是更新记录
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm()
    return render(request,'account/edit.html',{'user_form':user_form,
                                               'profile_form':profile_form})

@login_required()
def detail(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user_id=user.id)
    return render(request,'account/detail.html',{'user':user,'profile':profile})