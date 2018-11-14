from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail
import logging

@shared_task
def celery_send_email(subject,message,from_email,recipient_list,**kwargs):
    try:
        print('开始发送邮件...')
        send_mail(subject,message,from_email,recipient_list,**kwargs)
        print('发送邮件成功! ')
        return "email_send_success"
    except Exception as e:
        print('email_send_error: %s' % e)
