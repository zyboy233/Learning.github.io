# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 用来打开指定文件,并且对文件进行转码 防止出现乱码问题
import codecs
import json
import os
class XiaoshuoPipeline(object):
    def __init__(self):
        # w 写文件
        # w+读写文件 r+ 读写文件
        # 前者读写文件 如果文件不存在则创建
        # 后者读写文件 如果文件不存在 则抛出异常
        self.file = codecs.open(filename='book.json',mode='w+',encoding='utf-8')
        self.file.write('"list":[')
    # 如果想要将数据写入本地或者使用数据库的时候 这个方法需要保留
    def process_item(self, item, spider):
        # 将item对象转化成一个字典对象
        res = dict(item)
        # dumps将字典对象转化成字符串 ascii编码是否可用
        # 如果直接将字典形式的数据写入到文件当中  会发生错误
        # 所以需要将字典形式的值,转化为字符串写入文件
        str  = json.dumps(res,ensure_ascii=False)
        # 将数据写入到文件当中
        self.file.write(str)
        self.file.write(',\n')
        return item
    def open_spider(self,spider):
        print('爬虫开始')
    def close_spider(self,spider):
        # 删除文件当中最后一个字符
        # -1 表示偏移量
        # SEEK_END 定位到文件最后一个字符
        self.file.seek(-1,os.SEEK_END)
        # 开始执行
        self.file.truncate()

        self.file.seek(-1,os.SEEK_END)
        self.file.truncate()

        self.file.write(']')
        self.file.close()
        print('爬虫结束')
