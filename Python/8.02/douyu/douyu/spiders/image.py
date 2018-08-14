# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem

record = 1

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['api.douyucdn.cn']
    start_urls = ['http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset=1']

    def parse(self, response):
        responseJson = json.loads(response.text)
        print(responseJson)
        for obj in responseJson['data']:
            item = DouyuItem()
            img_src = obj['room_src']
            # print(img_src)
            item['img_src'] = [img_src]
            yield item
        global record
        record += 1
        next_url = 'http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset=' + str(record)
        yield scrapy.Request(next_url,callback=self.parse)


