# -*- coding: utf-8 -*-
import scrapy
from ..emailSpider import SendEmail
import datetime

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def start_requests(self):
        email = SendEmail()
        # 获取现在的时间
        body = '爬虫开始时间为:{}'.format(datetime.datetime.now())

        subject= '重要通知:明天放假'

        receiver = '451253127@qq.com'

        email.send_text_email(body,receiver,subject)

        yield scrapy.Request(url='https://www.baidu.com')
    def parse(self, response):
        pass


