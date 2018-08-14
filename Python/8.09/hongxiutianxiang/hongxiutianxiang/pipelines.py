# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy,codecs,os,json

class HongxiutianxiangPipeline(object):
    def __init__(self):
        self.file = codecs.open(filename='hongxiu.json',mode='w+',encoding='utf-8')
    def process_item(self, item, spider):
        res = dict(item)
        str = json.dumps(res,ensure_ascii=False)
        self.file.write(str)
        self.file.write('\n')

        return item
class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 请求图片的url
        yield scrapy.Request(url=item['img'][0],meta={'item':item})
    # 设置文件下载路径以及文件名字
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        bookName = item['title']
        path = bookName + '.jpg'
        return path