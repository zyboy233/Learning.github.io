# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhanzhangItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/tupian/meinvtupian.html']

    def parse(self, response):
        div_list = response.xpath('//div[@class="box picblock col3"]')
        for div in div_list:
            item = ZhanzhangItem()
            src = div.xpath('.//img/@src2').extract()[0]
            item['src'] = [src]
            yield item
        next_page = response.xpath('//a[@class="nextpage"]/@href').extract()
        if len(next_page) != 0:
            yield scrapy.Request(url='http://sc.chinaz.com/tupian/'+next_page[0],callback=self.parse)
