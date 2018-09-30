from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from myApp.models import EmailRecord
import random

def get_random_code(max_length=16):
    str='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiiopasdfghjklzxcvbnm7894561213'
    content = ''
    for x in range(max_length):
        content = content + random.choice(str)
    return content
def send_email(email,code=0,email_type = 'register'):
    if email_type == 'register':
        if code == 0:
            # 获取随机的激活码
            code = get_random_code()
            email_obj = EmailRecord()
            email_obj.code = code
            email_obj.email = email
            email_obj.save()
        # 发送邮件
        email_Subject = 'XX网账号激活'
        mail_content = '<h3>点击以下链接激活账号:</h3><br><a href="http://localhost:8000/login/active/{}">http://localhost:8000/login/active/{}</a>'.format(
            code, code)

        mail = EmailMultiAlternatives(email_Subject, mail_content, settings.EMAIL_HOST_USER, ['18537623991@163.com'])
        mail.content_subtype = 'html'
        res = mail.send()

        return res
    elif email_type == 'forget':
        email_Subject = 'XX网账号重置'
        mail_content = '<h3>点击以下链接重置密码:</h3><br><a href="http://localhost:8000/login/reset/{}">http://localhost:8000/login/reset/{}</a>'.format(
            email, email)

        mail = EmailMultiAlternatives(email_Subject, mail_content, settings.EMAIL_HOST_USER, ['18537623991@163.com'])
        mail.content_subtype = 'html'
        res = mail.send()

        return res