# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import re,json

class HuaSpider(scrapy.Spider):
    name = 'hua'
    allowed_domains = ['huaban.com']
    start_urls = ['http://huaban.com/favorite/beauty/']

    def parse(self, response):
        print(response.text)
        pattern = re.compile(r'"pins".*?= (.*?)app.page.*?ads',re.S)
        result = pattern.findall(response.text)[0][:-2]
        resultJson = json.loads(result)
        print('------------')
        print(resultJson)
        for item in resultJson:
            print(item)


