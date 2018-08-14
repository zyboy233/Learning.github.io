# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class DouguomeishiPipeline(object):
    def __init__(self):
        self.con = sqlite3.connect('meishiDB')
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists meishiTable(title text,author text,img text,href text,skip text)')
        self.con.commit()
    def process_item(self,item,spider):
        self.cursor.execute('insert into MeiShiTable VALUES ("{}","{},"{}","{}","{}")'.format(item['title'],item['author'],item['img'],item['href'],item['skip']))
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()