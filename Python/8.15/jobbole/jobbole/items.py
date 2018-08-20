# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst

# itemloader是分离数据的另一种方式 使用itemloader加载器
# 有这样一些优势:
# 1.默认使用xpath()/css()这种数据提取方式
# 是将数据的提取和数据的过滤等过程放在一个函数中
# 采用itemloader这种数据加载方式
# 可以将数据的提取和分离分成两部分
# 让代码更加清晰,代码更加整洁
# 2. 可以将数据的处理函数单独定义
# 可对单一数据使用多函数处理,便于代码复用

def changeTitle(value):
    value = '标题:' + value
    return value
def getNewtime(value):
    newTime = value.split('·')[0]
    newTime = newTime.strip()
    return newTime
def getNum(value):
    pattern = re.compile(r'\d+')
    result = re.findall(pattern,value)
    if result:
        return int(result[0])
    else:
        return 0
# 使用itemloader需要先继承
class ArticleItemLoader(ItemLoader):
    # default_output_processor 设置输出内容的类型
    # TakeFirst 获取所有数据当中的第一条
    # 默认返回的数据为一个列表 列表当中有一条数据
    # default_output_processor = ItemLoader.default_output_processor()
    default_output_processor = TakeFirst()
class JobboleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    title = scrapy.Field(
        # 如果函数一Map...开头,那么内部很可能是一个可迭代对象
        # 在此处,MapCompose括号里面可以追加多个参数,每个参数都是一个函数
        # 那么获取的内容会依次进入每个函数中执行
        input_processor = MapCompose(changeTitle,lambda x: x+'-------------------')
    )
    date_time = scrapy.Field(
        input_processor = MapCompose(getNewtime)
    )
    detail = scrapy.Field()
    dian_zan = scrapy.Field()
    book_mark_num = scrapy.Field(
        input_processor=MapCompose(getNum)
    )
    comment_num = scrapy.Field(
        input_processor=MapCompose(getNum)
    )
