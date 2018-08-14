# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import json
import codecs
import os


class ZhanzhangPipeline(object):
    def process_item(self, item, spider):
        return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        
        yield scrapy.Request(url=item['img'][0],meta={'dirname':item['dirname']})

    def file_path(self, request, response=None, info=None):
        filename = request.url.split('/')[-1]
        print('+++++++',filename)
        dirname = request.meta['dirname']
        print('========',dirname)
        path = '/%s/%s' % (dirname,filename)
        return path
class MyJsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('file.json',mode='w+',encoding='utf-8')
        self.file.write('"list":[')
    def process_item(self,item,spider):
        res = dict(item)
        str = json.dumps(res,ensure_ascii=False)
        self.file.write(str)
        self.file.write(',\n')

    def close_spider(self,spider):
        self.file.seek(-1,os.SEEK_END)
        self.file.truncate()

        self.file.seek(-1, os.SEEK_END)
        self.file.truncate()

        self.file.write(']')
        self.file.close()
