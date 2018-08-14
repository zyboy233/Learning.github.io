# -*- coding: utf-8 -*-
import scrapy
from ..items import NetbianItem
class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kmeinv/']

    def parse(self, response):
        img_src = response.xpath('//a[@id="img"]/img/@src')

        infos = response.xpath('//ul[@class="clearfix"]/li/a/@href')
        # print(info_url)
        if img_src:
            item = NetbianItem()
            img_src ='http://pic.netbian.com' + img_src.extract()[0]
            item['img_src'] = [img_src]
            yield item
        else:
            for info in infos:
                info_url = 'http://pic.netbian.com' + info.extract()
                yield scrapy.Request(info_url,callback=self.parse)
            next_page ='http://pic.netbian.com' +  response.xpath('//a[text()="下一页"]/@href').extract()[0]
            yield scrapy.Request(next_page,callback=self.parse)