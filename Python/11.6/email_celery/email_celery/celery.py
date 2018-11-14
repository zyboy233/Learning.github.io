from __future__ import absolute_import

import os
from celery import Celery

# 为celery程序设置DJANGO_SETTINGS_MODULE环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE','email_celery.settings')

app = Celery('email_celery')

# 从django的设置文件中导入celery的设置
app.config_from_object('django.conf:settings',namespace='CELERY')

# 从所有已经注册的app中加载任务模块(tasks)
app.autodiscover_tasks()
