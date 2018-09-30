from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from myApp.models import EmailRecord
import random

def newCode():
    str = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789'
    content = ''
    for x in range(16):
        content += random.choice(str)
    return content

def sendEmail(email,code=0,email_type='regist'):
    if email_type == 'regist':
        if code == 0:
            code = newCode()
            record_obj = EmailRecord()
            record_obj.code = code
            record_obj.email = email
            record_obj.save()

        subject = 'XX账号激活'
        content = '<h3>点击如下链接激活账号:</h3><a href="http://localhost:8000/login/active/{}">http://localhost:8000/active/login/{}</a>'.format(
            code, code)
        box = EmailMultiAlternatives(subject, content, settings.EMAIL_HOST_USER, ['18537623991@163.com'])
        box.content_subtype = 'html'
        res = box.send()
        return res
    elif email_type == 'forget':
        code = newCode()
        record_obj = EmailRecord()
        record_obj.code = code
        record_obj.email = email
        record_obj.save()

        subject = 'XX账号重置密码'
        content = '<h3>点击如下链接重置账号密码:</h3><a href="http://localhost:8000/login/reset/{}">http://localhost:8000/login/reset/{}</a>'.format(
            code, code)
        box = EmailMultiAlternatives(subject, content, settings.EMAIL_HOST_USER, ['451253127@qq.com'])
        box.content_subtype = 'html'
        res = box.send()
        return res
