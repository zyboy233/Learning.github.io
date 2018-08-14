# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json,os
from urllib.request import urlretrieve

class HongixuPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    def __init__(self):
        self.f = codecs.open('xiaoshuo.json', 'a', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"#确保中文显示正常
        self.f.write(lines)
        return item
    def open_spider(self,spider):
        print('------------------','json管道开始')
    def close_spider(self, spider):
        self.f.close()
        print('------------------','json管道结束')
class ImagesPipeline(object):
    def __init__(self):
        pass
    def process_item(self,item,spider):
        img_src = dict(item)['img_src']
        img_name = dict(item)['name']
        if not os.path.exists('d:/hongxiu'):
            os.mkdir('d:/hongxiu')
        os.chdir('d:/hongxiu')
        urlretrieve(img_src,'{}.jpg'.format(img_name))
        return item
    def open_spider(self,spider):
        print('------------------','images管道开始')
    def close_spider(self,spider):
        print('------------------','images管道结束')
