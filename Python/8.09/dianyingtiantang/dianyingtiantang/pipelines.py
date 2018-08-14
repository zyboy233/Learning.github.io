# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DianyingtiantangPipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipeline(object):
    def __init__(self):
        self.con = pymysql.connect(host='localhost',user='root',password='123456',db='dianyingtiantangDB',port=3306)
        self.cursor = self.con.cursor()
    def process_item(self,item,spider):
        sql = 'insert into dianyingtiantangTable VALUES ("{}","{}")'.format(item['title'],item['url'])
        self.cursor.execute(sql)
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()