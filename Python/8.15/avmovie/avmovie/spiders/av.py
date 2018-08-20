# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

from scrapy_redis.spiders import RedisSpider

from ..items import AvmovieItem


class AvSpider(RedisSpider):
    name = 'av'
    allowed_domains = ['javbooks.com']
    redis_key = 'avspider:start_urls'
    # start_urls = ['https://javbooks.com/serchinfo_uncensored/topicsbt/topicsbt_1.htm']
    # rpush avspider:start_urls https://javbooks.com/serchinfo_uncensored/topicsbt/topicsbt_6.htm
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    # 获取每页所有人的链接
    def parse(self, response):
        person_list = response.xpath('//div[@class="Po_u_topicCG"]/a/@href').extract()
        for person in person_list:
            print(person)
            yield scrapy.Request(url=person,callback=self.get_detail)

        # 获取下一页
        next_page = response.xpath('//a[text()="下一頁 > "]/@href').extract()
        if len(next_page) != 0:
            print(next_page[0])
            yield scrapy.Request(url=next_page[0],callback=self.parse)

    # 获取详情页
    def get_detail(self,response):
        img = response.xpath('//div[@class="info_cg"]/img/@src').get()
        name = response.xpath('//div[@id="title"]/b/text()').get()
        bt_url = response.xpath('//span[@class="content_bt_url"]/a/@href').extract()
        space_list = response.xpath('//div[@class="dht_dl_size_content"]/text()').extract()
        bt_str = ''
        if bt_url != 0:
            for bt,size in zip(bt_url,space_list):
                bt_str += '||' + bt + '('+size+')'

        item = AvmovieItem()
        item['img'] = img
        item['name'] = name
        item['bt_str'] = bt_str
        yield item