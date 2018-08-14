# -*- coding: utf-8 -*-
import scrapy
from ..items import DouguomeishiItem

class DouguoSpider(scrapy.Spider):
    name = 'douguo'
    allowed_domains = ['douguo.com']
    start_urls = ['https://www.douguo.com/caipu/%E4%B8%8B%E9%A5%AD%E8%8F%9C']

    def parse(self, response):
        dish_list = response.xpath('//div[@id="container"]/div[@class="cp_box"]')
        for dish in dish_list:
            img = dish.xpath('.//a/img/@src').extract_first('')
            title = dish.xpath('.//a/img/@alt').extract_first('')
            href = dish.xpath('.//a/@href').extract_first('')
            author = dish.xpath('.//div[@class="cp_msg"]/a[@class="cp_author"]/text()').extract()[1]
            author = author.replace(' ','')
            skip = dish.xpath('.//div[@class="cp_msg"]/p[@class="cp_cate"]/text()').extract_first('')
            print(img,title,href,author,skip)

            item = DouguomeishiItem()
            item['img'] = img
            item['title'] = title
            item['href'] = href
            item['author'] = author
            item['skip'] = skip
            yield item