# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'baiduSpider'
    # 允许爬虫的范围
    # allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # body为响应体
        # print(response.body)
        # 响应头
        # print(response.headers)
        # 获取当前状态
        # print(response.status)
        code = response.body.decode()
