#!/usr/bin/env python
# -*- coding: utf-8 -*-


from email.mime.text import MIMEText

from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
from email.mime.multipart import MIMEMultipart,MIMEBase
#格式化邮件，如果name包含中文需要进行编码
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#邮件对象
msg=MIMEMultipart()

from_addr=input('From:')
password=input('Password:')
smtp_server=input('SMTP server:')
to_addr=input('To:')
to_addr = list(to_addr.split(','))

#把From,To，和subject添加到邮件对象中
msg['From']=_format_addr('Python 爱好者 <%s>' % from_addr)
msg['To']=_format_addr('管理员 <%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候……','utf-8').encode()

#邮件正文是MIMEText
msg.attach(MIMEText('send with file...','plain','utf-8'))

#添加附件就是加上一个MIMEBase,从本地读取一个图片
with open('./thumb.jpg','rb') as f:
    #设置附件的MIME和文件名，这里是jpg类型
    mime=MIMEBase('image','jpg',filename='thumb.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='thumb.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    #添加到MIMEMultipart
    msg.attach(mime)

#SMTP默认段口号是25
server=smtplib.SMTP_SSL(smtp_server,465)

#打印和SMTP服务器交互信息
server.set_debuglevel(1)

#登陆
server.login(from_addr,password)
#一次可以发送多人，所以传入一个list
#邮件正文是一个str,as_string()把MIMEText对象变成str
server.sendmail(from_addr,to_addr,msg.as_string())

server.quit()

