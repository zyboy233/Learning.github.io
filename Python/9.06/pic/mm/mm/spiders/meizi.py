# -*- coding: utf-8 -*-
import scrapy
from ..items import MmItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['pic.ganbi888.com']
    start_urls = ['http://pic.ganbi888.com/category/dongfang/178/']

    def parse(self, response):
        # print(response.text)
        page_list = response.xpath('//div[@class="catagory-list"]/ul/li/a/@href').extract()
        for page in page_list:
            yield scrapy.Request(url=page,callback=self.get_img_with_url)
        next_page = response.xpath('//a[text()="后一页 »"]/@href').get()
        print(next_page,'==================================')
        if next_page:
           yield scrapy.Request(url=next_page,callback=self.parse)
    def get_img_with_url(self,response):
        title = response.xpath('//h1/a/text()').get()
        img_list = response.xpath('//div[@class="post-content"]/p/img/@src').extract()
        item = MmItem()
        item['title'] = title
        item['img_list'] = [img_list]
        yield item
