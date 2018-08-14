# -*- coding: utf-8 -*-
import scrapy
from ..items import ZimuzuItem

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['zimuzu.io']
    start_urls = ['http://www.zimuzu.io/resourcelist']

    def parse(self, response):
        # print(response.text)
        li_list = response.xpath('//div[@class="resource-showlist has-point"]/ul/li')
        for li in li_list:
            item = ZimuzuItem()
            name = li.xpath('.//h3[@class="f14"]/a/text()').extract()[0]

            point = li.xpath('.//span[@class="point"]').xpath('string(.)').extract()
            if point:
                point = point[0]
            else:
                point = ''
            tag_tv = li.xpath('.//strong[@class="tag tv"]/text()').extract()[0]

            status = li.xpath('.//font[@class="f4"]/text()').extract()[0]
            src ='http://www.zimuzu.io' + li.xpath('.//h3[@class="f14"]/a/@href').extract()[0]
            img_src = li.xpath('.//img/@src').extract()[0]

            item['name'] = name
            item['point'] = point
            item['tag_tv'] = tag_tv
            item['status'] = status
            item['src'] = src
            item['img_src'] = img_src

            yield item
        next_page =response.xpath('//a[text()="下一页"]/@href').extract()
        if len(next_page) == 0:
            print('没有下一页了...')
            return
        next_page ='http://www.zimuzu.io' + next_page[0]
        yield scrapy.Request(url=next_page,callback=self.parse)

