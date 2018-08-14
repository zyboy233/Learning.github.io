import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Email(object):
    def __init__(self):
        self.host = 'smtp.qq.com'
        self.port = '465'
        self.sender = '451253127@qq.com'
        self.receiver = '18537623991@163.com'
        self.password = 'juetgexalusfbhha'
    def sendemail(self,body,subject):
        message = MIMEMultipart('related')

        message_html = MIMEText('{}'.format(body),"plain","utf-8")
        message.attach(message_html)

        message_image = MIMEText(open('D:/taobao/1.jpg','rb').read(),'base64','utf-8')
        message_image['Content-disposition'] = 'attachment;filename="taobao.jpg"'
        message.attach(message_image)

        message_csv = MIMEText(open('D:/taobao/taobao.csv', 'rb').read(), 'base64', 'utf-8')
        message_csv['Content-Disposition'] = 'attachment;filename="taobao.csv"'
        message.attach(message_csv)

        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = subject

        try:
            email_client = smtplib.SMTP_SSL(self.host,self.port)
            login_result = email_client.login(self.sender,self.password)
            print('开始登陆,',login_result)
            # 如果有登陆信息 并且登录信息里面的第一条状态吗为235 说明登陆成功
            if login_result and login_result[0] == 235:
                print('登陆成功')
                email_client.sendmail(self.sender,self.receiver,message.as_string())
                print('发送成功')
            else:
                print('登陆失败')
        except Exception as e:
            print('邮件发送失败',e)