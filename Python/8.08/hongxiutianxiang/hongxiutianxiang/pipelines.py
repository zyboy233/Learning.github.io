# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class HongxiutianxiangPipeline(object):
    def process_item(self, item, spider):
        return item

class HongXiuDBPipeline(object):
    def open_spider(self,spider):
        self.con = sqlite3.connect('hongxiuDB')
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists bookTable(name text,author text,img text,intro text)')
        self.con.commit()
    def process_item(self,item,spider):
        print('--------------------------------------')
        self.cursor.execute('insert into bookTable VALUES ("{}","{}","{}","{}")'.format(item['name'],item['author'],item['img'],item['intro']))
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()