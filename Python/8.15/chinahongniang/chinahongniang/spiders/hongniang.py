# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ChinahongniangItem

# 注意:此处为单机爬虫 而不是分布式爬虫
# 创建该文件的命令:
    # scrapy genspider -t crawl hongniang hongniang.com
class HongniangSpider(CrawlSpider):
    name = 'hongniang'
    allowed_domains = ['hongniang.com']
    start_urls = ['http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=1&province=%E6%B2%B3%E5%8D%97&city=%E9%83%91%E5%B7%9E&page=1']

    # 只爬取第一页相关数据 与网站无关或者不是第一页 不爬取
    page_link = LinkExtractor(allow=r'http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=1&province=%E6%B2%B3%E5%8D%97&city=%E9%83%91%E5%B7%9E&page=1')
    # 获取个人主页
    person_link = LinkExtractor(allow=r'http://www.hongniang.com/user/member/id/\d+')
    rules = (
        Rule(page_link, follow=True),
        # scrapy写法 callback = self.xxxx
        # crawl写法 callback = 'xxx'
        Rule(person_link,callback='get_detail',follow=False)
    )
    def get_detail(self,response):
        print('----------------')

        header = response.xpath('//img[@id="pic_"]/@src').get()
        print(header)
        name = response.xpath('//div[@class="name nickname"]/text()').extract_first('')
        print(name)
        age = response.xpath('//div[@class="info2"]//ul[1]/li[1]/text()').get()
        print(age)
        height = response.xpath('//div[@class="info2"]//ul[2]/li[1]/text()').get()
        print(height)

        item = ChinahongniangItem()
        item['header'] = header
        item['name'] = name
        item['age'] = age
        item['height'] = height
        yield item

    def parse_item(self, response):
        i = {}
        # itemloader
        # add_value
        # add_xpath
        # add_css
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
