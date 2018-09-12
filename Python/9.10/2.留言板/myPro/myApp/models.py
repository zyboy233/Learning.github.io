from django.db import models

# Create your models here.

class Message(models.Model):
    m_id = models.AutoField(primary_key=True)
    # TextField和CharField都是文本样式  基本没有差别
    # 不过
    # TextField 理论上无限长度
    # CharField 需要指定长度
    m_name = models.TextField()
    m_email = models.CharField(max_length=50)
    m_address = models.CharField(max_length=50)
    m_message = models.TextField()

