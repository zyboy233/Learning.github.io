from django.shortcuts import render

from django.http import HttpResponse
from app_celery.tasks import celery_send_email

import datetime
# Create your views here.

# 计时
def count_time(func):
    def int_time(*args,**kwargs):
        start_time = datetime.datetime.now()
        func(*args)
        end_time = datetime.datetime.now()
        total_time = (end_time - start_time).total_seconds()
        print('计时: %s 秒' % total_time)
        return HttpResponse('Send email successful! ')
    return int_time

@count_time
def add_task_send_email(request):
    celery_send_email.delay('邮件的主题','这是邮件内容','18537623991@163.com',['451253127@qq.com'])
    # return HttpResponse('Send email successful! ')