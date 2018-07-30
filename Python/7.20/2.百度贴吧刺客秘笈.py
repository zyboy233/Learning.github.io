import re
from urllib.request import Request,urlopen
import sqlite3

class DBManager(object):
    con = None
    cursor = None
    @classmethod
    def createTable(cls):
        cls.con = sqlite3.connect('barDB')
        cls.cursor = cls.con.cursor()
        cls.cursor.execute('create table if not exists barTable(user text,content text)')
        cls.con.commit()
    @classmethod
    def insert_into_barTable(cls,data=[]):
        cls.con = sqlite3.connect('barDB')
        cls.cursor = cls.con.cursor()
        cls.cursor.execute('insert into barTable(user,content) VALUES ("{}","{}")'.format(data[0],data[1]))
        cls.con.commit()
    @classmethod
    def closeDB(cls):
        cls.cursor.close()
        cls.con.close()
class DataManager(object):
    def to_new_data(self,data):
        content = data
        # print(content)
        content = content.replace('\u3000','').replace('<br>','').replace('            ','')

        pattern = re.compile(r'<img.*?>',re.S)
        pattern1 = re.compile(r'<a.*?>',re.S)
        pattern2 = re.compile(r'</a>',re.S)
        pattern3 = re.compile(r'<div.*?>',re.S)
        pattern4 = re.compile(r'<embed.*?>', re.S)
        content = pattern.sub('',content)
        content = pattern1.sub('',content)
        content = pattern2.sub('',content)
        content = pattern3.sub('',content)
        content = pattern4.sub('',content)
        return content

class BarSpider(object):
    def __init__(self):

        self.insert_data = DBManager()
        self.dataTools = DataManager()


    def download_code(self,page):
        url = 'https://tieba.baidu.com/p/4685013359?pn={}'.format(page)

        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        request = Request(url,headers=headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
            # print(code)
        except Exception as e:
            print('获取失败:',e)
            return None
        else:
            return code
    def get_pages_from_code(self,code):
        pattern = re.compile(r'<div class="content clearfix".*?<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)
        return int(result[0])
    def get_data_from_code(self,code):
        pattern = re.compile(r'<li class="d_name".*?<a.*?>(.*?)</a>.*?<cc>.*?>(.*?)</div>',re.S)
        code = pattern.findall(code)
        # print(code)
        for user,content in code:
            list1 = []
            # print(content)
            pattern = re.compile(r'\n',re.S)
            pattern2 = re.compile(r'<img.*?>',re.S)
            user = pattern.sub('',user)
            user = pattern2.sub('',user)
            content = self.dataTools.to_new_data(content)
            list1.append(user)
            list1.append(content)
            print(list1)
            self.insert_data.insert_into_barTable(list1)






DBManager.createTable()


spider = BarSpider()

code = spider.download_code(1)
num = spider.get_pages_from_code(code)
for i in range(1,num+1):
    code = spider.download_code(i)
    spider.get_pages_from_code(code)
    spider.get_data_from_code(code)

