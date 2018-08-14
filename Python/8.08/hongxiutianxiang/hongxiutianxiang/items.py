# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HongxiutianxiangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    intro = scrapy.Field()
    pass
