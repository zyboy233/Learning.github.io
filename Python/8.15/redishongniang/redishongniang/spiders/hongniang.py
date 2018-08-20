# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

from ..items import RedishongniangItem
class HongniangSpider(RedisCrawlSpider):
    name = 'hongniang'
    allowed_domains = ['hongniang.com']
    redis_key = 'hongniangspider:start_urls'

    page_link = LinkExtractor(allow=r'http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=1&province=%E6%B2%B3%E5%8D%97&city=%E9%83%91%E5%B7%9E&page=1')
    person_link = LinkExtractor(allow=r'http://www.hongniang.com/user/member/id/\d+')

    rules = (
        Rule(page_link,follow=True),
        Rule(person_link,callback='get_detail',follow=False)
    )

    def get_detail(self,response):
        print('----------------')

        header = response.xpath('//img[@id="pic_"]/@src').get()
        print(header)
        name = response.xpath('//div[@class="name nickname"]/text()').extract_first('')
        print(name)
        # age = response.xpath('//div[@class="info2"]//ul[1]/li[1]/text()').get()
        # print(age)
        # height = response.xpath('//div[@class="info2"]//ul[2]/li[1]/text()').get()
        # print(height)

        item = RedishongniangItem()
        item['header'] = header
        item['name'] = name
        # item['age'] = age
        # item['height'] = height
        yield item
