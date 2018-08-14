# -*- coding: utf-8 -*-
import scrapy
from ..items import MeizituItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['mmjpg.com']
    start_urls = ['http://mmjpg.com/']

    # 获取所有类型
    def parse(self, response):
        nav_list = response.xpath('//div[@class="subnav"]/a/@href').extract()[1:]
        type_list = response.xpath('//div[@class="subnav"]/a/text()').extract()[1:]
        for type,nav in zip(type_list,nav_list):
            yield scrapy.Request(url=nav,meta={'type':type},callback=self.get_page_with_url)
    # 获取类型页面
    def get_page_with_url(self,response):
        li_list = response.xpath('//div[@class="pic"]/ul/li')
        type = response.meta['type']
        for li in li_list:
            href = li.xpath('.//a/@href').extract_first('')
            name = li.xpath('.//a/img/@alt').extract_first('')
            yield scrapy.Request(url=href,meta={'type':type,'name':name},callback=self.get_info_with_href)
        # 获取该类型下一页并回调
        next_page = response.xpath('//a[text()="下一页"]/@href').extract_first('')
        if len(next_page)!=0:
            yield scrapy.Request(url='http://www.mmjpg.com'+next_page,meta={'type':type},callback=self.get_page_with_url)
    # 获取每位妹子写真
    def get_info_with_href(self,response):
        img = response.xpath('//div[@class="content"]/a/img/@src').extract_first('')
        type = response.meta['type']
        name = response.meta['name']
        num = response.xpath('//div[@class="page"]/em/text()').extract_first('')

        item = MeizituItem()
        item['img'] = [img]
        item['type'] = type
        item['name'] = name
        item['num'] = num
        yield item
        # 获取妹子下一张图片
        next_page = response.xpath('//a[text()="下一张"]/@href').extract()
        if len(next_page) != 0:
            next_page = 'http://www.mmjpg.com' + next_page[0]
            yield scrapy.Request(url=next_page,meta={'type':type,'name':name},callback=self.get_info_with_href)
