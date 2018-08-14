# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhanzhangItem

class IconSpider(scrapy.Spider):
    name = 'icon'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/']

    def parse(self, response):
        icon_url = response.xpath('//li[@class="nos"]/a[text()="图标"]/@href').extract_first('')
        full_url = 'http://sc.chinaz.com' + icon_url
        yield scrapy.Request(url=full_url,callback=self.parse_icon_url)

    def parse_icon_url(self,response):
        a_list = response.xpath('//ul[@class="pngblock imgload"]/li/p/a')
        for a in a_list:
            href = a.xpath('@href').extract_first('')
            title = a.xpath('@alt').extract_first('')
            # yield scrapy.Request(url=href,callback=self.get_detail_with_url)
            # meta负责传递往下个方法发送的内容
            yield scrapy.Request(url=href,callback=self.get_detail_with_url,meta={'title':title})
            # 获取全部图标的下载链接
            # next_url = response.xpath('')
    def get_detail_with_url(self,response):
        title = response.meta['title']
        # print(title)
        img_list = response.xpath('//div[@class="png_sl"]/div/img/@src').extract()
        print(img_list)
        for img in img_list:
            item = ZhanzhangItem()
            item['title'] = title
            item['img'] = [img]
            # print('----------------------------------------')
            yield item