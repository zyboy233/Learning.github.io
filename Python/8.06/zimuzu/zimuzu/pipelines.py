# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os,csv
from urllib.request import urlretrieve

class ZimuzuPipeline(object):
    def process_item(self, item, spider):
        return item

class CsvPipeline(object):
    def __init__(self):
        self.csv = open('D:/zimuzu/renren.csv','a',newline='')
    def process_item(self,item,spider):
        print(item)
        item_dict = dict(item)
        item_dict.pop('img_src')
        keys = []
        for key in item_dict.keys():
            keys.append(key)
        print(keys)
        writer = csv.DictWriter(self.csv,fieldnames=keys)
        writer.writerow(item_dict)
        return item
class ImagesPipeline(object):
    def __init__(self):
        pass
    def process_item(self,item,spider):
        img_name = dict(item)['name']
        img_src = dict(item)['img_src']
        if not os.path.exists('D:/zimuzu'):
            os.mkdir('D:/zimuzu')
        os.chdir('D:/zimuzu')
        urlretrieve(img_src,'{}.jpg'.format(img_name))
        return item
    def open_spider(self,spider):
        print('-----------------images管道开始')
    def close_spider(self,spider):
        print('-----------------images管道结束')