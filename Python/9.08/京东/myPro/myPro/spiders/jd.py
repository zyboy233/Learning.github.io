# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from ..items import MyproItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['search.jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=小米&enc=utf-8']
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.page = 1
    def parse(self, response):
        print(response.text)
        goods = response.xpath('//ul[@class="gl-warp clearfix"]//div[@class="gl-i-wrap"]')
        print(len(goods))
        for good in goods:
            img ='https:'+ good.xpath('.//div[@class="p-img"]/a/img/@src').extract_first('')
            price = good.xpath('.//div[@class="p-price"]//i/text()').get()
            title = good.xpath('.//div[@class="p-name p-name-type-2"]/a/@title').get()
            commit = good.xpath('.//div[@class="p-commit"]//a/text()').get()
            shop = good.xpath('.//div[@class="p-shop"]//a/@title').get()

            item = MyproItem()
            item['food']='小米'
            item['title'] = title
            item['price'] = price
            item['shop'] = shop
            item['img'] = [img]
            item['commit'] = commit
            yield item
        self.page += 2
        next_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&page={}'.format('小米',str(self.page))
        if self.page != 11:
            yield scrapy.Request(url=next_url,callback=self.parse)


