# -*- coding: utf-8 -*-
import scrapy
from ..items import WomenItem

class GirlsSpider(scrapy.Spider):
    name = 'girls'
    allowed_domains = ['jpxgyw.com']
    start_urls = ['https://www.jpxgyw.com/']
    record = 2

    def parse(self, response):
        href_list = response.xpath('//div[@class="lm10"]/a/@href').extract()
        for href in href_list[1:]:
            href = 'https://www.jpxgyw.com' + href
            yield scrapy.Request(url=href,callback=self.get_nav_with_href)

    def get_nav_with_href(self,response):
        girl_list = response.xpath('//div[@class="biank1"]/a/@href').extract()
        for girl in girl_list:
            href = 'https://www.jpxgyw.com' + girl
            yield scrapy.Request(url=href,callback=self.get_girl_with_href)
        next_page = response.xpath('//a[text="尾页"]/@href').extract()
        if len(next_page) != 0:
            yield scrapy.Request(url=next_page[0],callback=self.parse)

    def get_girl_with_href(self,response):
        name = response.xpath('//p[@style="text-align: center"]/img/@alt').extract()[0]
        src_list = response.xpath('//p[@style="text-align: center"]/img/@src').extract()
        for src in src_list:
            src = 'https://www.jpxgyw.com' + src

            item = WomenItem()
            item['name'] = name
            item['src'] = [src]
            print(name,src)

            yield item

        next_page = response.xpath('//div[@class="page"]/a[last()]/@href')
        if len(next_page) != 0:
            print(next_page)
            yield scrapy.Request(url='https://www.jpxgyw.com'+next_page.extract()[0],callback=self.parse)
