# 目的
# 封装邮件发送的逻辑 不管哪一个项目或者文件需要发送邮件
# 只需要引入这个文件  并且实现其方法就能发送邮件

import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class SendEmail(object):
    def __init__(self):
        self.email_host = 'smtp.qq.com'
        self.email_port = '465'
        self.email_serder = '451253127@qq.com'
        self.email_receiver = '451253127@qq.com'
        # 注意 此处为授权码
        self.email_password = 'juetgexalusfbhha'

    # 发送纯文本文件
    def send_text_email(self,body,receiver,subject):
        # 1. 内容主体
        # 2. 内容类型
        # 3. 编码方式
        message_text = MIMEText(body,'plain','utf-8')
        message_text['From'] = self.email_serder
        message_text['To'] = receiver
        message_text['Subject'] = subject

        try:
            email_client = smtplib.SMTP_SSL(self.email_host,self.email_port)
            login_result = email_client.login(self.email_serder,self.email_password)
            print('开始登陆,',login_result)
            # 如果有登陆信息 并且登录信息里面的第一条状态吗为235 说明登陆成功
            if login_result and login_result[0] == 235:
                print('登陆成功')
                email_client.sendmail(self.email_serder,receiver,message_text.as_string())
                print('发送成功')
            else:
                print('登陆失败')
        except Exception as e:
            print('邮件发送失败',e)

    def send_image_email(self):
        pass
    def send_file_email(self):
        pass


