# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import QiubaiItem
from scrapy_redis.spiders import RedisSpider

class QiuSpider(RedisSpider):
    name = 'qiu'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/imgrank/page/1/']
    redis_key = 'myspider:start_urls'

    def parse(self, response):
        # print(response.text)
        div = response.xpath('//div[@id="content-left"]/div')
        # div_list = response.xpath('.//div[@class="author clearfix"]/a/h2/text()').extract()
        content_list = div.xpath('.//div[@class="content"]/span').extract()
        img_list = div.xpath('.//div[@class="thumb"]/a/img/@src').extract()
        tag_pattern = re.compile('<.*?>')
        for content,img_src in zip(content_list,img_list):
            item = QiubaiItem()
            content = tag_pattern.sub('',content).replace('\n','')
            img_src = 'https:' + img_src

            item['content'] = content
            item['img_src'] = [img_src]
            yield item

        next_page = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract()
        print('-------------------------------------', next_page)
        if len(next_page) == 0:
            print("没有下一页了")
            return
        yield scrapy.Request(url='https://www.qiushibaike.com' + next_page[0],callback=self.parse)
