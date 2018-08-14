# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import csv,os
from urllib.request import urlretrieve
from .sendEmail import Email

class TaobaospiderPipeline(object):
    def process_item(self, item, spider):
        return item
class MyExcelPipeline(object):
    def __init__(self):
        self.file = open('D:/taobao/taobao.csv','w',newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['name','price','shop'])
    def process_item(self,item,spider):
        row = [item['name'],item['price'],item['shop']]
        self.writer.writerow(row)
        return item
    def close_spider(self,spider):
        email = Email()
        email.sendemail('淘宝IOS数据线信息', '数据线')

class MyImagePipeline(ImagesPipeline):
    # def get_media_requests(self, item, info):
    #     yield scrapy.Request(url=item['img'][0],meta={'item':item})
    # def file_path(self, request, response=None, info=None):
    #     print('---------------------------')
    #     print(request.meta['item']['name'])
    #     fileName = request.meta['item']['name']
    #     path = '/{}.png'.format(fileName)
    #     return path
    def process_item(self,item,spider):
        os.chdir('D:/taobao')
        urlretrieve(item['img'][0],item['name']+'.jpg')
        return item