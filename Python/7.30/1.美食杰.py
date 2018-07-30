import requests
import lxml
from bs4 import BeautifulSoup
import sqlite3
from fake_useragent import UserAgent

class MeishiDB(object):
    con = None
    cursor = None
    def openDB(self):
        self.con = sqlite3.connect('meishiDB')
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists MeiShiTable (name text,src text)')
        self.con.commit()
    def add_info_to_db(self,name,src):
        self.cursor.execute('insert into MeiShiTable VALUES ("{}","{}")'.format(name,src))
        self.con.commit()
    def close(self):
        self.cursor.close()
        self.con.close()
class MeiShiJie(object):
    def __init__(self):
        self.headers = UserAgent()
        self.DB = MeishiDB()
    def spider(self):
        # 打开数据库和创建数据表
        self.DB.openDB()
        code = self.get_code_with_url('https://www.meishij.net/chufang/diy/')
        self.DB.close()
    def get_code_with_url(self,url):
        headers = {
            'User-Agent':self.headers.random
        }
        response = requests.get(url,headers=headers).text
        # print(response)
        code = BeautifulSoup(response,'lxml')
        self.get_content_with_code(code)
    def get_content_with_code(self,code):
        divList = code.select('div.listtyle1')
        for div in divList:
            img_alt = div.select('img')[0]['alt']
            print(img_alt)
            img_src = div.select('img')[0]['src']
            print(img_src)
            self.DB.add_info_to_db(img_alt,img_src)
        self.get_next_page_with_code(code)
    def get_next_page_with_code(self,code):
        next_url = code.select('a.next')
        if len(next_url) == 0:
            print('最后一页')
            return
        self.get_code_with_url(next_url[0]['href'])

meishi = MeiShiJie()
meishi.spider()