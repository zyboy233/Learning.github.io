# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhanzhangItem

class ZhanSpider(scrapy.Spider):
    name = 'zhan'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/tubiao/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="pngblock imgload"]/li')
        for li in li_list:
            href = li.xpath('.//p/a/@href').extract_first('')
            dirname = li.xpath('.//p/a/@alt').extract_first('')
            # print(href,dirname)
            yield scrapy.Request(url=href,meta={'dirname':dirname},callback=self.get_imgs_with_href)

        next_page = response.xpath('//a[text()="下一页"]/@href').extract()
        if len(next_page) != 0:
            yield scrapy.Request(url='http://sc.chinaz.com/tubiao/'+next_page[0],callback=self.parse)
    def get_imgs_with_href(self,response):
        dirname = response.meta['dirname']
        img_list = response.xpath('//div[@class="png_pic"]/img/@src').extract()
        for img in img_list:
            item = ZhanzhangItem()
            item['dirname'] = dirname
            item['img'] = [img]
            yield item