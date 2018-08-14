# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZimuzuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    point = scrapy.Field()
    tag_tv = scrapy.Field()
    status = scrapy.Field()
    src = scrapy.Field()
    img_src = scrapy.Field()