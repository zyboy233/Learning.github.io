# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item
class MyImagePipeline(ImagesPipeline):
    # 获取请求图片url
    def get_media_requests(self, item, info):
        print('---------------')
        yield scrapy.Request(url=item['img'][0],meta={'item':item})
    # 设置保存路径
    def file_path(self, request, response=None, info=None):
        type = request.meta['item']['type']
        name = request.meta['item']['name']
        num = request.meta['item']['num']

        print('++++++++++++++++')
        return '/{}/{}/{}.jpg'.format(type,name,num)