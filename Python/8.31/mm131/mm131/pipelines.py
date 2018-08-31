# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class Mm131Pipeline(object):
    def process_item(self, item, spider):
        return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['meizi_url'][0],meta={'item':item})
    def file_path(self, request, response=None, info=None):
        type = request.meta['item']['type']
        name = request.meta['item']['name']
        imgname = request.meta['item']['meizi_url'][0].split('/')[-1]

        return '{}/{}/{}'.format(type,name,imgname)