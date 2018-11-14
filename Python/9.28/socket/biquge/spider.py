import requests
import datetime
import smtplib

from lxml import etree
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class Biquge(object):
    """
    爬取小说内容
    """
    def __init__(self):
        # 圣墟： http://www.biquge.com.tw/11_11850/
        # 飞剑问道： http://www.biquge.com.tw/18_18820/
        self.url = ['http://www.biquge.com.tw/11_11850/','http://www.biquge.com.tw/18_18820/']
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

    def spider(self):
        total_novel = '-------------小说分割线------------\n'
        for url in self.url:
            total_novel += self.get_code_with_url(url) + '\n-------------小说分割线------------\n'
        email = EmailNovel()
        email.send(total_novel)
    def get_code_with_url(self,url):
        response = requests.get(url,headers=self.headers)
        root = etree.HTML(response.content.decode('gbk'))
        today_date = str(datetime.datetime.now())[:10]
        date_update = root.xpath('//div[@id="info"]/p[last()-1]/text()')[0]
        if date_update == '最后更新：' + today_date:
            page_url = root.xpath('//p[text()="最新章节："]/a/@href')[0]
            page_url = url + page_url
            return self.get_info_with_url(page_url)
        return ''
    def get_info_with_url(self,url):
        response = requests.get(url,headers=self.headers)

        root = etree.HTML(response.content.decode('gbk'))
        content = root.xpath('//div[@id="content"]/text()')
        novel = ''
        for index in content:
            if  index != '\r\n':
                novel += index.replace(r'    ','')
        return novel

class EmailNovel(object):
    """发送邮件"""
    def __init__(self):
        self.HOST='smtp.163.com'
        self.SUBJECT = '今日小说内容！'
        self.FROM = '18537623991@163.com'
        self.TO = '451253127@qq.com'
    def send(self,content):
        message = MIMEMultipart('related')
        message_html = MIMEText(content)
        message.attach(message_html)

        message['From'] = self.FROM
        message['To'] = self.TO
        message['Subject'] = self.SUBJECT
        email_client = smtplib.SMTP_SSL()
        email_client.connect(self.HOST,'465')
        result = email_client.login(self.FROM,'zy520520')
        print(result)
        email_client.sendmail(from_addr=self.FROM,to_addrs=(self.TO,),msg=message.as_string())
        email_client.close()
if __name__ == '__main__':
    spider = Biquge()
    spider.spider()