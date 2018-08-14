# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import HongxiuItem
class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/all?gender=2&catId=-1']

    def parse(self, response):
        type_list = response.xpath('//ul[@type="category"]/li/a/@href').extract()
        del type_list[0]
        for type in type_list:
            url = 'https://www.hongxiu.com' + type
            split = re.compile(r'.*?catId=(.*?)&.*?',re.S)
            catId = re.findall(split,url)
            yield scrapy.Request(url=url,meta={'type':catId[0]},callback=self.get_content_with_type_url)

    def get_content_with_type_url(self,response):
        catId = response.meta['type']
        for page_num in range(1,11):
            # https://www.hongxiu.com/all?pageSize=10&gender=2&catId=-1&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=5
            url = 'https://www.hongxiu.com/all?pageNum' + str(page_num) + '?pageSize=10&gender=2&catId=' + catId +'&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0'
            yield scrapy.Request(url=url,callback=self.get_book_with_url)

    def get_book_with_url(self,response):
        detail_list = response.xpath('//div[@class="book-info"]/h3/a/@href').extract()
        for book_detail in detail_list:
            url = 'https://www.hongxiu.com' + book_detail
            yield scrapy.Request(url=url,callback=self.get_detail_with_url)

    def get_detail_with_url(self,response):
        type = response.xpath('//div[@class="crumbs-nav center1020"]/span/a[2]/text()').extract_first('')
        name = response.xpath('//div[@class="book-info"]/h1/em/text()').extract_first('')
        author = response.xpath('//div[@class="book-info"]/h1/a/text()').extract_first('')
        total = response.xpath('//p[@class="total"]/span/text()').extract_first('') + response.xpath('//p[@class="total"]/em/text()').extract_first('')
        love = response.xpath('//p[@class="total"]/span[2]/text()').extract_first('') + response.xpath('//p[@class="total"]/em[2]/text()').extract_first('')
        point = response.xpath('//p[@class="total"]/span[3]/text()').extract_first('') + response.xpath('//p[@class="total"]/em[3]/text()').extract_first('')
        introduce = response.xpath('//p[@class="intro"]/text()').extract_first('')
        url = 'https:' + response.xpath('//div[@class="book-img"]/a/img/@src').extract_first('')
        url = url.replace('\r','')

        item = HongxiuItem()
        item['type'] = type
        item['name'] = name
        item['author'] = author
        item['total'] = total
        item['love'] = love
        item['point'] = point
        item['introduce'] = introduce
        item['url'] = [url]
        yield item