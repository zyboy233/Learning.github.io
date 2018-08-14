# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy,os
from urllib.request import urlretrieve
from scrapy.pipelines.images import ImagesPipeline

class WomenPipeline(object):
    def process_item(self, item, spider):
        return item

class MyPipeline(object):
    def process_item(self,item,spider):
        fileName = item['name']
        name = item['src'][0].split('/')[6].split('.')[0]
        if not os.path.exists('D:/women/{}'.format(fileName)):
            os.mkdir('D:/women/{}'.format(fileName))
        os.chdir('D:/women/{}'.format(fileName))
        urlretrieve(url=item['src'][0],filename=name+'.jpg')
        return item
# class MyImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         yield scrapy.Request(url=item['src'][0],meta={'item':item})
#     def file_path(self, request, response=None, info=None):
#         fileName = request.meta['item']['name']
#         name = request.url.split('/')[6].split('.')[0]
#         print(fileName,name)
#         path = '{}/{}.jpg'.format(fileName,name)
#         return path