# -*- coding: utf-8 -*-
import scrapy
from ..items import NetbianItem

class BianSpider(scrapy.Spider):
    name = 'bian'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kdongman/']

    def parse(self, response):
        href_list = response.xpath('//ul[@class="clearfix"]/li/a/@href').extract()
        for href in href_list:
            href = 'http://pic.netbian.com' + href
            yield scrapy.Request(url=href,callback=self.get_img_with_href)
        next_page = response.xpath('//a[text()="下一页"]/@href').extract()
        if len(next_page) != 0:
            yield scrapy.Request(url='http://pic.netbian.com'+next_page[0],callback=self.parse)
    def get_img_with_href(self,response):
        name = response.xpath('//div[@class="photo-hd"]/h1/text()').extract_first('')
        img ='http://pic.netbian.com' + response.xpath('//div[@class="photo-pic"]/a/img/@src').extract_first('')
        item = NetbianItem()
        item['name'] = name
        item['img'] = [img]
        yield item