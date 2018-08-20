# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver
from ..items import ArticleItemLoader
from scrapy_redis.spiders import RedisSpider
from ..items import ZhilianItem

class JobSpider(RedisSpider):
    name = 'job'
    allowed_domains = ['sou.zhaopin.com']
    # start_urls = ['https://sou.zhaopin.com/?jl=489']
    redis_key = 'jobspider:start_urls'

    # lpush jobspider:start_urls https://sou.zhaopin.com/?jl=489

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        # print(response.text)
        div_list = response.xpath('//div[@class="listItemBox clearfix"]')
        for div in div_list:

            item_loder = ArticleItemLoader(item=ZhilianItem(),response=response)

            title = div.xpath('.//span[@class="job_title"]/@title').get()
            commpany = div.xpath('.//div[@class="commpanyName"]/a/text()').get()
            salary = div.xpath('.//p[@class="job_saray"]/text()').get()
            add = div.xpath('.//ul[@class="job_demand"]/li[1]/text()').get()
            # print(title)
            # print(commpany)
            # print(salary)
            # print(add)

            item_loder.add_value('title',title)
            item_loder.add_value('commpany',commpany)
            item_loder.add_value('salary',salary)
            item_loder.add_value('add',add)

            # item = ZhilianItem()
            # item['title'] = title
            # item['commpany'] = commpany
            # item['salary'] = salary
            # item['add'] = add

            item = item_loder.load_item()

            yield item


