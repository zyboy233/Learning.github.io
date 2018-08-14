# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MeishijiePipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost',user='root',password='123456',db='meishijieDB',port=3306,charset='utf8')
        self.cursor = self.db.cursor()
    def process_item(self,item,spider):
        print('---------------------------')
        sql = 'insert into meishijieTable VALUES ("{}","{}","{}")'.format(item['title'],item['img_src'],item['gx'])
        self.cursor.execute(sql)
        self.db.commit()
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()