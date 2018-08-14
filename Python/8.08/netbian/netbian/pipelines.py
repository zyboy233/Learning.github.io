# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import sqlite3
import scrapy

class NetbianPipeline(object):
    def process_item(self, item, spider):
        return item
class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img'][0],meta={'item':item})
    def file_path(self, request, response=None, info=None):
        fileName = request.meta['item']['name']+'.jpg'
        return '%s' % fileName
class sqlPipeline(object):
    def __init__(self):
        self.con = sqlite3.connect('bianDB')
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists bianTable(name text,img text)')
        self.con.commit()
    def process_item(self,item,spider):
        self.cursor.execute('insert into bianTable (name,img) VALUES ("{}","{}")'.format(item['name'],item['img'][0]))
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()