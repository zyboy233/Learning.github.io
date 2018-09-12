from django.shortcuts import render , reverse
from .models import Message
from django.http import HttpResponse
# Create your views here.
def add(request):
    # 如果请求方式为get 那么当前网页是通过在浏览器输入网址进来的
    if request.method == 'GET':
        # reverse()函数可以对url进行反响映射
        # 之前是通过url地址找到指定的网页
        # 现在通过reverse()函数根据url名字来找到url地址
        # add为urls.py中写到的url的name值
        url = reverse('add')
        return render(request,'add.html',{'url':url})
    else:
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        message = request.POST['message']

        message_model = Message()
        message_model.m_name = name
        message_model.m_email = email
        message_model.m_address = address
        message_model.m_message = message
        message_model.save()

        allInfo = Message.objects.all()
        return render(request,'showAll.html',{'allInfo':allInfo,'judge':1})
def showAll(request):
    allInfo = Message.objects.all()
    return render(request,'showAll.html',{'allInfo':allInfo,'judge':1})
def update(request):
    # 如果通过修改按钮或者通过网址的方式进入的更新页面
    # 那么默认进入页面的请求方式为get
    if request.method == "GET":
        url = reverse('update')
        return render(request,'update.html',{'url':url})
    elif request.method == 'POST':
        url = reverse('update')
        m_id = request.POST['id']
        m_name =request.POST['name']
        m_address = request.POST['address']
        m_email = request.POST['email']
        m_message = request.POST['message']

        message_update = Message.objects.get(m_id=m_id)
        message_update.m_name = m_name
        message_update.m_address = m_address
        message_update.m_email = m_email
        message_update.m_message = m_message
        message_update.save()

        allInfo = Message.objects.all()
        return render(request,'showAll.html',{'allInfo':allInfo,'judge':1})
def delete(request):
    if request.method == 'GET':
        return render(request,'delete.html')
    else:
        id = request.POST['id']
        msg_del = Message.objects.get(m_id=id).delete()
        allInfo = Message.objects.all()
        return render(request,'showAll.html',{'allInfo':allInfo,'judge':1})
def select(request):
    if request.method == 'GET':
        return render(request,'select.html')
    else:
        if request.POST['id'] and request.POST['name']:
            msg = Message.objects.filter(m_id=request.POST['id'],m_name=request.POST['name'] )
        elif request.POST['id']:
            msg = Message.objects.filter(m_id=request.POST['id'])
        else:
            msg = Message.objects.filter(m_name=request.POST['name'])
        if len(msg) !=0:
            return render(request,'showAll.html',{'allInfo':msg,'judge':1})
        else:
            return render(request,'showAll.html',{'allInfo':msg,'judge':0})