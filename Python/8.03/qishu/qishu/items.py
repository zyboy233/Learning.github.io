# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QishuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    clickNum = scrapy.Field()
    fileSize = scrapy.Field()
    bookType = scrapy.Field()
    updateTime = scrapy.Field()
    bookStatus = scrapy.Field()
    bookAuthor = scrapy.Field()
    imageUrl = scrapy.Field()
    downloadUrl = scrapy.Field()
