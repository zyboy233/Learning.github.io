# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from ..items import AvmovieItem

class AvSpider(scrapy.Spider):
    name = 'av'
    allowed_domains = ['jmvbt.com']
    start_urls = ['https://jmvbt.com/serchinfo_uncensored/753/performerbt_1.htm']
    def __init__(self):
        self.driver = webdriver.PhantomJS()
    def parse(self, response):
        href_list = response.xpath('//div[@class="Po_u_topic_title"]/a/@href').extract()
        actor = response.xpath('//div[@id="DL_Options"]/text()').extract_first('')
        for href in href_list:
            yield scrapy.Request(url=href,meta={'actor':actor},callback=self.get_info_with_href)
    def get_info_with_href(self,response):
        actor = response.meta['actor']
        title = response.xpath('//div[@id="title"]/b/text()').extract_first('')
        print('------------------',title)
        img = response.xpath('//div[@id="info"]/div/img/@src').extract_first('')
        num = response.xpath('//font[@color="#A63600"]/text()').extract_first('')
        bt_list = response.xpath('//div[@class="dht_dl_title_content"]/span/a/@href').extract()
        item = AvmovieItem()
        item['actor'] = actor
        item['title'] = title
        item['img'] = [img]
        item['num'] = num
        item['bt_list'] = bt_list

        yield item