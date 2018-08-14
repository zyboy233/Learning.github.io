# -*- coding: utf-8 -*-
import scrapy
from ..items import ImagenetItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['pic.netbian.com']
    # 请求最开始的url
    start_urls = ['http://pic.netbian.com/4kmeishi/']

    def parse(self, response):
        # 根据响应来找到制定的内容 现在找的是img的src属性
        img_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@src')
        # print(img_list)
        # 找到多个属性值 遍历
        for img in img_list:
            # 使用在items.py中定义的数据模型item
            item = ImagenetItem()
            img_src ='http://pic.netbian.com' + img.extract()
            # print(img_src)
            # 将下载地址放入数据模型中
            # 下载地址要包在list当中
            item['img_src'] = [img_src]
            # 将数据传输给管道
            yield item

        next_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()
        if len(next_url) != 0:
            url = 'http://pic.netbian.com' + next_url[0]
            # 将url传给scrapy.Request  得到的结果继续用self.parse继续处理
            yield scrapy.Request(url,callback=self.parse)