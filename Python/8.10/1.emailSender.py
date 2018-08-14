# smtp simple mail transfer protocol 简单邮件传传输协议
# lib library
import smtplib
import email
# MIME 多用于邮件扩充协议
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

HOST = 'smtp.qq.com'

SUBJECT = '今天是2018年8月10号,是我18岁生日'
# 注意 发件人的邮箱必须开启smtp协议
FROM = '451253127@qq.com'
# 设置收件人的邮箱(可以一次性发送给多人)
TO = '451253127@qq.com,18537623991@163.com'
# related使用内嵌资源的方式  将邮件发送给对方
# 邮件信息 内容为空


message = MIMEMultipart('related')

# ---------------------发送文本
# 发送邮件主体到对方的邮箱中
# 参数
# 1. 发送的内容 内容必须是字符串
# 2. 内容的类型 文本类型默认是plain
# 3. 内容的编码方式 使用utf-8编码
# message_html= MIMEText('今天是星期五,好开心','plain','utf-8')
message_html = MIMEText('<h2 style="color:red;font-size:100px">明天是周六,我是去学习呢还是去学习呢</h2><img src="cid:small">',"html","utf-8")
# 将邮件内容 装入到邮件信息当中
message.attach(message_html)

# ---------------------发送图片
# rb 读取二进制文件
image_data= open('timg.gif','rb')
# 设置读取获取的二进制数据
message_image = MIMEImage(image_data.read(),'base64')
# 关闭打开的文件
image_data.close()
message_image.add_header('Content-ID','small')
# 添加图片文件到邮件信息当中
# message.attach(message_image)

# --------------------------------发送图片的第二种方式
message_image = MIMEText(open('timg.gif','rb').read(),'base64','utf-8')
message_image['Content-disposition'] = 'attachment;filename="happy.gif"'
message.attach(message_image)
# --------------------添加文件
# 将一个xls文件作为内容发送到对方的邮箱
# 读取excel文件是以rb形式进行读取的
# 是一个二进制内容,对二进制文件需要设置默认的编码形式
# 对于MIMEText()来说 默认的编码形式就是base64
# 如果对于二进制文件来说 没有设置base64进行编码 则附件呈现乱码
message_xls = MIMEText(open('table.xls','rb').read(),'base64','utf-8')
# 设置文件在附件当中的名字
message_xls['Content-Disposition'] = 'attachment;filename="test111.xls"'
#
message.attach(message_xls)

# 设置邮件发送人
message['From'] = FROM
# 设置邮件收件人
message['To'] = TO
# 设置邮件标题
message['Subject'] = SUBJECT
# 获取简单邮件传输协议的证书
email_client = smtplib.SMTP_SSL()
# 设置发件人邮箱的域名和端口  端口为465
email_client.connect(HOST,'465')
# 密码为网易邮箱的第三方授权码
result = email_client.login(FROM,'buploemfyiqkcahc')

print('登陆结果',result)
# 发送邮件
# message = MIMEMultipart('related') 是一个对象,msg要求字符串
email_client.sendmail(from_addr=FROM,to_addrs=TO.split(','),msg=message.as_string())
# 关闭发送邮件客户端
email_client.close()


