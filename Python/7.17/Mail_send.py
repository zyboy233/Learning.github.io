#!/usr/bin/env python
# -*- coding: utf-8 -*-


from email.mime.text import MIMEText

from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
from urllib.request import urlopen
import json,requests

# 天气
def getWeatherInfo():
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E%E5%B8%82&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    response = requests.get(url)
    dataJson = json.loads(response.text)
    msg = "\n"

    for data in dataJson["results"]:
        for index in data["index"]:
            msg = msg+index["des"]+'\n'
        wd = data["weather_data"][0]
        date = wd["date"]
        msg1 = "地点：郑州，日期：" + date
        msg =msg1+ "\n温度：" + wd["temperature"] +"，天气：" + wd["weather"] + "，风力：" + wd["wind"] + "\n温馨提示："+msg
        return msg

#格式化邮件，如果name包含中文需要进行编码
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#用utf-8保证多语言兼容
msg=MIMEText('hello,send by Python...\n {}'.format(getWeatherInfo()),'plain','utf-8')
from_addr=input('From:')
password=input('Password:')
smtp_server=input('SMTP server:')
to_addr=input('To:')
to_addr = list(to_addr.split(','))

#把From,To，和subject添加到MIMEText中
msg['From']=_format_addr('Python 爱好者 <%s>' % from_addr)
msg['To']=_format_addr('管理员 <%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候……','utf-8').encode()

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


