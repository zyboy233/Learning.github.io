import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','learncelery.settings')
app = Celery('learncelery')

# CELERY_ 作为前缀, 在settings文件中配置
app.config_from_object('django.conf:settings',namespace='CELERY')

# 到django的各个app下自动发现tasks.py任务脚本
app.autodiscover_tasks()