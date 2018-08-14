# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import DianyingtiantangItem

class DianyingSpider(scrapy.Spider):
    name = 'dianying'
    allowed_domains = ['ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/index.html']

    def parse(self, response):
        href_list = response.xpath('//div[@class="co_area2"]//td/a[2]/@href').extract()
        for href in href_list:
            href = 'http://www.ygdy8.net' + href
            yield scrapy.Request(url=href,callback=self.get_info_with_href)
    def get_info_with_href(self,response):
        code = response.text
        # print(code)
        pattern = re.compile(r'style="FONT-SIZE: 12px".*?名　(.*?) <br />',re.S)
        title = pattern.findall(code)[0]
        # title = response.xpath('//span[@style="FONT-SIZE: 12px"]/p/').extract()
        url = response.xpath('//td[@style="WORD-WRAP: break-word"]/a/@href').extract_first('')
        print(title)
        print(url)

        item = DianyingtiantangItem()
        item['title'] = title
        item['url'] = url
        yield item