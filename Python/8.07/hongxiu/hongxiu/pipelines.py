# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import json

class HongxiuPipeline(object):
    def __init__(self):
        self.file = codecs.open(filename='book.json',mode='w+',encoding='utf-8')
        self.file.write('"book_list":[')
    def process_item(self, item, spider):
        res = dict(item)
        str = json.dumps(res,ensure_ascii=False)
        self.file.write(str)
        self.file.write(',\n')
        return item
    def open_spider(self,spider):
        print("++++++++++++++++++++++++++++++")
    def close_spider(self,spider):
        self.file.seek(-1,os.SEEK_END)
        self.file.truncate()
        print('---------------------------------')
        self.file.seek(-1,os.SEEK_END)
        self.file.truncate()

        self.file.write(']')
        self.file.close()