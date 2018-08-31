# -*- coding: utf-8 -*-
import scrapy
from ..items import Mm131Item


class MmSpider(scrapy.Spider):
    name = 'mm'
    allowed_domains = ['mm131.com']
    start_urls = ['http://mm131.com/']

    def parse(self, response):
        navlist = response.xpath('//div[@class="nav"]/ul/li/a/@href').extract()[1:]
        for nav in navlist:
            yield scrapy.Request(nav,callback=self.get_nav_with_url)
    def get_nav_with_url(self,response):
        type = response.xpath('//dt[@class="public-title"]/a[last()]/text()').get()
        aList = response.xpath('//dl[@class="list-left public-box"]/dd')[0:-1]
        for a in aList:
            name = a.xpath('.//text()').get()
            urlpage = a.xpath('.//@href').get()
            print(name,urlpage)
            yield scrapy.Request(urlpage,meta={'base_url':response.url,'filename':name,'type':type},callback=self.get_per_page_with)
        next_page = response.xpath('//dd[@class="page"]/a[text()="下一页"]/@href').get()
        if next_page != None:
            yield scrapy.Request(response.url+next_page,callback=self.get_nav_with_url)
    def get_per_page_with(self,response):
        type = response.meta['type']
        filename = response.meta['filename']
        base_url = response.meta['base_url']
        meizi_url =response.xpath('//div[@class="content-pic"]/a/img/@src').get()

        item = Mm131Item()
        item['type'] = type
        item['name'] = filename
        item['meizi_url'] = [meizi_url]
        yield item

        next_page = response.xpath('//div[@class="content-page"]/a[text()="下一页"]/@href').get()
        if(next_page != None):

            next_page = base_url + next_page
            print(next_page,'++++++++++++++++++')
            yield scrapy.Request(next_page,meta={'type':type,'base_url':response.meta['base_url'],'filename':response.meta['filename']},callback=self.get_per_page_with)