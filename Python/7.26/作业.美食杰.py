# 1. 美食杰网站爬取封面图片,菜谱名及人气
# 以 "莴笋炒蛋（2047人气)" 形式存入数据库

from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,urlretrieve
import os,shutil
import sqlite3

# 数据库操作
class DBManager(object):
    con = None
    cursor = None
    @classmethod
    def createTable(cls):
        cls.con = sqlite3.connect('Msj')
        cls.cursor = cls.con.cursor()
        cls.cursor.execute('create table if not exists food(title text,src text)')
        cls.con.commit()
    @classmethod
    def insert_data(cls,title,src):
        cls.cursor.execute('insert into food VALUES ("{}","{}")'.format(title,src))
        cls.con.commit()
    @classmethod
    def closeDB(cls):
        cls.cursor.close()
        cls.con.close()
class Msj(object):
    def __init__(self):
        self.base_url = 'https://www.meishij.net/chufang/diy/?&page=1'
        self.DBmanager = DBManager()
        self.pagedir = 1

    def spider(self):
        self.DBmanager.createTable()
        if os.path.exists('D:/meishij'):
            shutil.rmtree('D:/meishij')
        os.mkdir('D:/meishij')
        os.chdir('D:/meishij')
        self.get_code_with_url(self.base_url)
        self.DBmanager.closeDB()
    def get_code_with_url(self,url):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        request = Request(url,headers=headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
            self.get_page_with_code(code)
        except Exception as e:
            print('获取失败:',e)
    def get_page_with_code(self,code):
        # print(code)
        soup = BeautifulSoup(code,'lxml')
        info = soup.select('.clearfix img')
        hots = soup.select('.c1 span')

        print(info,hots)
        os.mkdir('Page{}'.format(self.pagedir))
        os.chdir('Page{}'.format(self.pagedir))
        for data,hot in zip(info,hots):
            title = data.get('alt').replace('|','')
            src = data.get('src')
            hot = hot.get_text().replace(' ','').split('论')[1]
            print(title,src,hot)
            self.DBmanager.insert_data(title+'('+hot+')',src)
            urlretrieve(src,title+'('+hot+').jpg')
        os.chdir(os.path.pardir)
        next_page = soup.select('.next')
        if len(next_page)==0:
            print('没有下一页了')
            return
        next_page = next_page[0]
        next_page_url = next_page.get('href')
        self.pagedir +=1
        print(next_page)
        self.get_code_with_url(next_page_url)

msj = Msj()
msj.spider()
