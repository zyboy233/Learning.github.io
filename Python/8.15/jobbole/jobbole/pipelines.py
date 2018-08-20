# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JobbolePipeline(object):
    # def __init__(self):
    #     self.con = pymysql.connect(host='localhost',
    #                                user='root',
    #                                password='123456',
    #                                db='jobbole',
    #                                port=3306)
    #     self.cursor=self.con.cursor()
    # def process_item(self, item, spider):
    #     self.cursor.execute('insert into job(img,title,date_time,detail_url,dian_zan,book_mark_num,comment_num) VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(item['img'],item['title'],item['date_time'],item['detail'],item['dian_zan'],item['book_mark_num'],item['comment_num']))
    #     self.con.commit()
    #     return item
    # def close_spider(self,spider):
    #     self.cursor.close()
    #     self.con.close()
    def process_item(self,item,spider):
        return item