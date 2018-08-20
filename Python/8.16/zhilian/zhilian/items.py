# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst

def salary_deal(value):
    if 'K' in value:
        value_max = value.split('-')[1].split('K')[0]
        value_min = value.split('-')[0].split('K')[0]
        value = value_min +'/'+ value_max +'K'
    else:
        value = value
    return value
class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    commpany = scrapy.Field()
    salary = scrapy.Field(
        input_processor = MapCompose(salary_deal,)
    )
    add = scrapy.Field()
