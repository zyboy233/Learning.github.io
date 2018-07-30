
import re
from urllib.request import urlopen,Request
import sqlite3

# 专门处理各种数据 使其符合要求
class DataManager(object):
    # 该方法负责修改数据 去除不必要的内容
    def update_new_data(self,oldData):
        # print(oldData)
        name = oldData[0]
        name = name.strip('\n')

        content = oldData[2]
        content = content.strip('\n')
        # 去除<br/>
        pattern = re.compile(r'<br/>')
        content = pattern.sub('',content)
        newData = (name,oldData[1],content,oldData[3],oldData[4])
        return newData

class DBManager(object):
    con = None
    cursor = None
    @classmethod
    # 创建数据库
    def create_db_and_table(cls):
        cls.con = sqlite3.connect('qbDB')
        cls.cursor = cls.con.cursor()
        cls.cursor.execute('create table if not exists qbTable(name text,age text,content text,enjoy text,comment text)')
        cls.con.commit()
    @classmethod
    # 添加数据到数据库
    def insert_info_to_table(cls,receiveData):
        
        cls.cursor.execute('insert into qbTable VALUES ("{}","{}","{}","{}","{}")'.format(receiveData[0],receiveData[1],receiveData[2],receiveData[3],receiveData[4]))
        cls.con.commit()
    @classmethod
    # 关闭数据库
    def close_db(cls):
        cls.cursor.close()
        cls.con.close()

class QSBKSpider(object):
    def __init__(self):
        # 设置基本网址 基本网址为所有需要爬虫的共同部分
        self.base_url = 'https://www.qiushibaike.com/hot/page/'
        # 设置爬虫的用户标识
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # 创建一个数据管理的实例对象dataTool
        # 并使其作为QSBKSpider的属性
        self.dataTool = DataManager()
    def get_code_from_url(self,index):
        # 拼接完整的路径
        url = self.base_url + str(index) + '/'
        # 设置请求的url和请求头信息
        request = Request(url,headers=self.headers)
        # 获取响应信息
        response = urlopen(request)
        try:
            # 读取响应信息并解码
            code = response.read().decode()
        except Exception as e:
            print('获取信息失败',e)
            return None
        else:
            return code
    def get_userfull_info_from_code(self,code):
        # print(code)
        pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
        result = pattern.findall(code)
        # result获取所有的抓取的内容的总和
        for oldData in result:
            # oldData 为元组(姓名  年龄  内容 喜欢数  评论数)
            # 更新旧值得到一个新值
            newData = self.dataTool.update_new_data(oldData)
            # 插入数据库和表
            DBManager.insert_info_to_table(newData)


# 创建数据库
DBManager.create_db_and_table()

qbSpider = QSBKSpider()
# # 获取网页源码并转码
# code = qbSpider.get_code_from_url(1)
# # 提取网页数据
# qbSpider.get_userfull_info_from_code(code)

for x in range(1,11):
    code = qbSpider.get_code_from_url(x)
    qbSpider.get_userfull_info_from_code(code)
DBManager.close_db()

