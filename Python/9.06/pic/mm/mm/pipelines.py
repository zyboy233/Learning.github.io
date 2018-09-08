# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class MmPipeline(object):
    def process_item(self, item, spider):
        return item
class myImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img in item['img_list'][0]:
            yield scrapy.Request(url=img,meta={'title':item['title']})
    def file_path(self, request, response=None, info=None):
        title = request.meta['title']
        file_name = request.url.split(r'/')[-1]
        return '高清/{}/{}'.format(title,file_name)
