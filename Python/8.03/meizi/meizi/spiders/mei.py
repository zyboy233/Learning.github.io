# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
import scrapy
from ..items import MeiziItem
import os
import random

class MeiSpider(scrapy.Spider):
    name = 'mei'
    allowed_domains = ['rentiyishu55.com']
    start_urls = ['http://www.rentiyishu55.com']

    def parse(self, response):
        nav_list = response.xpath('//ul[@style="margin:0px;"]/li[@class="lin"]/a/@href').extract()[0:3]
        for nav in nav_list:
            nav = 'http://www.rentiyishu55.com/' + nav
            yield scrapy.Request(url=nav,callback=self.get_infos_with_nav)

    def get_infos_with_nav(self,response):
        infos = response.xpath('//ul[@class="photo"]/li/a/@href').extract()
        current_url = response.url

        for info in infos:
            info = current_url + info
            print('----------------')
            yield scrapy.Request(url=info,callback=self.get_pages_with_info)

        next_page =current_url + response.xpath('//a[text()="下一页"]/@href').extract()[0]
        yield scrapy.Request(url=next_page,callback=self.get_infos_with_nav)
    def get_pages_with_info(self,response):
        dir = response.xpath('//ul[@style="margin:8px;"]/h2/text()').extract()[0]
        try:
            os.mkdir('D:/meizi/{}'.format(dir))
        except:
            print('')
        finally:
            os.chdir('D:/meizi/{}'.format(dir))
        next_page =response.xpath('//a[text()="下一页"]/@href').extract()
        src_list = response.xpath('//ul[@class="file"]/img/@src').extract()
        if len(next_page) == 0:
            return
        else:
            for src in src_list:
                src = src.replace('\r','')
                item = MeiziItem()
                item['img_src'] = [src]
                urlretrieve(src,filename=str(random.randint(1,999999999999999))+'.jpg')
                # yield item
            yield scrapy.Request(url=response.url+next_page[0],callback=self.get_pages_with_info)