# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from ..items import TaobaospiderItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180809&ie=utf8']
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        print('================================')
        print(response)
        div_info = response.xpath('//div[@class="info-cont"]')
        print('======')
        print(div_info)
        for div in div_info:
            title = div.xpath('.//div[@class="title-row "]/a/text()').extract_first('')
            price = div.xpath('.//div[@class="sale-row row"]/div/span[2]/strong/text()').extract_first('')
            print('---------------------------------')
            print(title)
            print(price)
            item = TaobaospiderItem()
            item['title'] = title
            item['price'] = price

            yield item
    def closed(self, reason):
        print(u'爬虫关闭了, 原因：',reason)
        self.driver.quit()