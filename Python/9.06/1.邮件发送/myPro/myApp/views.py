from django.shortcuts import render
from django.http import HttpResponse
# 引入发送邮件的模块
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.conf import settings
# Create your views here.

def sendEmail(request):
    return render(request,'index.html')

def send_email(request):
    if request.method == 'POST':
        # 值1:邮件标题
        # 值2:邮件主体
        # 值3:发件人
        # 值4:收件人
        res = send_mail('关于国庆放假通知','上级领导{}通知,放假7天'.format('习大大'),
                        settings.EMAIL_HOST_USER,('451253127@qq.com',),)
        if res == 1:
            return HttpResponse('邮件发送成功')
        else:
            return HttpResponse('邮件发送失败')
    else:
        return render(request,'index.html')
def send_mass_email(request):
    message1 = ('物流信息','您的包裹已丢失',settings.EMAIL_HOST_USER,['451253127@qq.com','1311173658@qq.com'])

    message2 = ('物流信息','您的包裹又找到了',settings.EMAIL_HOST_USER,['451253127@qq.com','1311173658@qq.com'])

    res = send_mass_mail((message1,message2))

    if res == 2:
        return HttpResponse('多封邮件发送成功')
    else:
        return HttpResponse('多封邮件发送失败')
def send_html(request):

    html_message = '<a href="http://www.baidu.com">百度</a>'
    res = EmailMultiAlternatives('商品链接','请点击下面的链接'+html_message,settings.EMAIL_HOST_USER,['451253127@qq.com'])

    res.content_subtype = 'html'

    result = res.send()
    return HttpResponse(result)