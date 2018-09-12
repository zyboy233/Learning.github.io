# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    food = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    commit = scrapy.Field()
