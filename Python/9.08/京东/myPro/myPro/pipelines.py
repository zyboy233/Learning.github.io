# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
# from scrapy.exporters import JsonItemExporter
import json
import codecs

class MyproPipeline(object):
    def process_item(self, item, spider):
        return item
class myImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img'][0],meta={'item':item})
    def file_path(self, request, response=None, info=None):
        food = request.meta['item']['food']
        title = request.meta['item']['title']
        return '{}/{}.jpg'.format(food,title)
class myJsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('jd.json','w+',encoding='utf-8')
    def process_item(self,item,spider):
        dic = dict(item)
        str = json.dumps(dic,ensure_ascii=False)
        self.file.writer(str)
        self.file.writer(',\n')
        return item
    def close_spider(self,spider):
        self.file.close()