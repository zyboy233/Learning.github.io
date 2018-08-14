# -*- coding: utf-8 -*-

# 项目要求：
# 1.获取淘宝任意一个类别的商品信息
# 2.将商品名称，价格 ，店铺 三个信息存储到excel中
# 3.爬虫结束时，将excel以及获取的商品中任意一个商品的
#   图片一起发送到自己的邮箱

import scrapy
from selenium import webdriver
from ..items import TaobaospiderItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['s.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%E6%95%B0%E6%8D%AE%E7%BA%BF+ios&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180810&ie=utf8']
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        div_list = response.xpath('//div[contains(@class,"J_MouserOnverReq")]')
        for div in div_list:
            img ='https:' + div.xpath('.//a[@class="pic-link J_ClickStat J_ItemPicA"]/img/@data-src').extract_first('')
            print(img)
            name = div.xpath('.//a[@class="pic-link J_ClickStat J_ItemPicA"]/img/@alt').extract_first('')
            price = div.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()').extract_first('')
            shop = div.xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[last()]/text()').extract_first('')
            print(name,price,shop)

            item = TaobaospiderItem()
            item['img'] = [img]
            item['name'] = name
            item['price'] = price
            item['shop'] = shop

            yield item
