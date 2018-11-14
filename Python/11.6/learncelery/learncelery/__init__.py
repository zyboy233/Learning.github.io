from __future__ import absolute_import
from learncelery.celery import app as celery_app

# 保证celery app总能在django引用启动时启动
__all__ = ['celery_app']