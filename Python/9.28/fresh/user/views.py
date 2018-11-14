import datetime

from django.shortcuts import render,redirect,HttpResponse
from django.http.response import JsonResponse,HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.core.paginator import Paginator

from user.models import UserModel,CollectGoodsModel
from user.forms import UserRegisterForm,UserLoginForm
from goods.models import GoodsModel
from user.utils import login_required
from order.models import OrderModel
# Create your views here.

# 只接受post请求
def register_post(request):
    """只接受post请求的注册接口"""
    if request.method == 'POST':
        user = UserRegisterForm(request.POST)
        # print(user)
        if not user.is_valid():
            # valid = user.is_valid()
            return JsonResponse(user.errors.get_josn_data,safe=False)
    user = UserLoginForm()
    return render(request,'user/register_post.html',{'user':user})

def register(request):
    """注册接口"""
    if request.method == 'POST':
        # 忽略参数为空
        username = request.POST.get('username','')
        if not username:
            return JsonResponse({'error':'请输入用户名'})
        password = request.POST.get('password','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        email = request.POST.get('email','')

        # 新建用户
        user = UserModel()
        user.username = username
        # 密码加密后存储
        user.password = make_password(password)
        user.phone = phone
        user.address = address
        user.email = email
        user.save()
        return HttpResponseRedirect('/account/login')
    return render(request,'user/register.html')

def login(request):
    """登陆接口"""
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        # 当jizhu有值的时候,就是这个复选框被勾选的时候的值1,没有的话是0
        jizhu = request.POST.get('jizhu',0)

        # 根据用户名查询用户对象
        user = UserModel.objects.filter(username=username)

        # 判断, 如果没有查询到说明用户错误 ,查到判断密码是否正确
        # 密码错误,则返回登陆界面并且提示密码错误
        if user:
            user = user[0]
            # 检查密码是否正确
            is_password = check_password(password,user.password)
            if not is_password:
                # 密码错误
                return render(request,'user/login.html',{'username':username,'is_password':1,'is_user':0})
            else:
                # 密码正确
                # 先生成一个response对象
                next_url = request.COOKIES.get('next_url','/goods/index/')
                response = HttpResponseRedirect(next_url)
                # 记住用户名
                # 设置cookie
                if jizhu != 0:
                    response.set_cookie('username',username)
                else:
                    response.set_cookie('username','',max_age=-1) # max_age指的是过期时间,为-1时立即过期
                # 把用户id和username放入到session中
                request.session['user_id'] = user.id
                request.session['username'] = username
                print(request.session)
                return response
            # return render(request,'user/index.html',{'username':user.username})
        else:
            return render(request,'user/login.html',{'username':username,'is_user':1,'is_password':0})
    cookie = request.COOKIES
    # 查看cookie
    print(cookie)
    return render(request,'user/login.html')

def logout(request):
    del request.session['user_id']
    del request.session['username']
    return redirect('/account/login/')

@login_required
def info(request):
    """用户个人信息"""
    user_id = request.session['user_id']
    user = UserModel.objects.get(id=request.session['user_id'])
    user_info = {
        'username':user.username,
        'phone':user.phone,
        'address':user.address
    }
    # 从session中拿到商品的id的列表(在商品详情里面写入session的)
    print(request.session.items())
    goods_id_list = request.session.get(str(user_id),[])
    # 用户最近浏览的商品记录
    goods_list = []
    # 通过遍历商品id列表,拿到商品对象组成的一个有序的商品列表对象
    for goods_id in goods_id_list:
        goods_list.append(GoodsModel.objects.get(id=goods_id))
    context = {'user_info':user_info,'goods_list':goods_list,'title':'用户中心'}
    return render(request,'user/user_center_info.html',context)

@login_required
def all_order(request,page_num):
    """全部订单"""
    # 查询当前登陆用户所有登陆信息
    user_id = request.session.get('user_id')
    all_order = OrderModel.objects.filter(user_id=user_id).order_by('-id')
    # 每一页展示2个
    paginator = Paginator(all_order,2)
    page = paginator.page(page_num)

    context = {
        'page':page,
        'page_num':page_num,
        'title':'全部订单'
    }
    return render(request,'user/user_center_order.html',context)

@login_required
def address(request):
    user_id = request.session.get('user_id')
    collectgoods_list = CollectGoodsModel.objects.filter(user_id=user_id)
    if collectgoods_list:
        collectgoods = collectgoods_list[0]
    else:
        collectgoods = 0
    if request.method == 'POST':
        if collectgoods == 0:
            collectgoods = CollectGoodsModel()
            collectgoods.user = UserModel.objects.get(id=user_id)
        person_name = request.POST.get('person_name')
        detail_address = request.POST.get('detail_address')
        postcode = request.POST.get('postcode')
        tel = request.POST.get('tel')
        collectgoods.person_name = person_name
        collectgoods.detail_address = detail_address
        collectgoods.postcode = postcode
        collectgoods.tel = tel
        collectgoods.is_used = 1
        collectgoods.save()
    context = {
        'collectgoods':collectgoods,
        'title':'收货地址'
    }
    return render(request,'user/user_center_address.html',context)

def upload(request):
    """上传接口"""
    if request.method == 'GET':
        return render(request,'upload.html')
    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        ext = myfile.name.split('.')[-1]
        myfilename = 'text.'+ext
        with open(myfilename,'wb') as fp:
            for chunk in myfile.chuncks():
                fp.write(chunk)
        return JsonResponse({'result':'success'})

def handle_wx(request):
    # 微信公众平台绑定验证
    echostr = request.GET.get('echostr','')
    return HttpResponse(echostr,content_type="text/plain")