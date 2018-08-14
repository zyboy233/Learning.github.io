# -*- coding: utf-8 -*-
import scrapy
from ..items import MeishijieItem

class MeiSpider(scrapy.Spider):
    name = 'mei'
    allowed_domains = ['meishij.net']
    start_urls = ['https://www.meishij.net/chufang/diy/langcaipu/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="listtyle1"]')
        for div in div_list:
            title = div.xpath('.//a/@title').extract_first('')
            img_src = div.xpath('.//a/img/@src').extract_first('')
            gx = div.xpath('.//strong[@class="gx"]/span/text()').extract_first('')
            item = MeishijieItem()
            item['title'] = title
            item['img_src'] = img_src
            item['gx'] = gx

            yield item

        next_page = response.xpath('//a[text()="下一页"]/@href')
        if len(next_page) != 0:
            yield scrapy.Request(url=next_page.extract()[0],callback=self.parse)