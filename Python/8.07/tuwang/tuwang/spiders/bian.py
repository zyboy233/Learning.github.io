# -*- coding: utf-8 -*-
import scrapy
from ..items import TuwangItem

class BianSpider(scrapy.Spider):
    name = 'bian'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kfengjing/']

    def parse(self, response):
        img_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@src').extract()
        # print(img_list)
        for img in img_list:
            item = TuwangItem()
            url = 'http://pic.netbian.com' + img
            item['url'] = [url]

            yield item
        next_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()
        if len(next_url) != 0:
            yield scrapy.Request(url= 'http://pic.netbian.com' + next_url[0],callback=self.parse)