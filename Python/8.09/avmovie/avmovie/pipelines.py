# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import codecs,json,os
from urllib.request import urlretrieve

class AvmoviePipeline(object):
    def process_item(self, item, spider):
        return item
class textPipeline(object):
    def process_item(self,item,spider):
        actor = item['actor']
        title = item['title']
        img = item['img']
        bt_list = str(item['bt_list'])
        if not os.path.exists('D:/av/{}'.format(actor)):
            os.mkdir('D:/av/{}'.format(actor))
        os.chdir('D:/av/{}'.format(actor))
        os.mkdir('{}'.format(title))
        os.chdir('{}'.format(title))
        urlretrieve(url=img[0],filename=title+'.jpg')
        f = open('{}.text'.format(title),mode='w',encoding='utf-8')
        f.write(bt_list+'\n')
        f.close()
        return item