# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class TaobaospiderPipeline(object):
    def __init__(self):
        self.con = sqlite3.connect('taobaoDB')
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists taobaoTable(title text,price text)')
    def process_item(self, item, spider):

        self.cursor.execute('insert into taobaoTable VALUES ("{}","{}")'.format(item['title'],item['price']))
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.commit()