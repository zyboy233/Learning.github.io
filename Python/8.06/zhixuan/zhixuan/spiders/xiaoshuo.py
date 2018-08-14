# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhixuanItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['zxcs8.com']
    start_urls = ['http://www.zxcs8.com/sort/26']

    def parse(self, response):
        url_list = response.xpath('//dl[@id="plist"]/dt/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url=url,callback=self.get_info_with_url)
    def get_info_with_url(self,response):
        sub_url = response.xpath('//p[@class="filetit"]/a/@href').extract()[0]
        yield scrapy.Request(url=sub_url,callback=self.get_info_with_sub_url)
    def get_info_with_sub_url(self,response):
        item = ZhixuanItem()
        name = response.xpath('//div[@class="content"]/h2/text()').extract()[0]
        src = response.xpath('//span[@class="downfile"]/a[text()="线路一"]/@href').extract()[0]
        item['name'] = name
        item['src'] = [src]
        yield item