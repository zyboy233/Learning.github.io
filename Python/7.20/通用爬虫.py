import re
from urllib.request import urlopen,Request
import sqlite3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 数据库操作
class DBManager(object):
    con = None
    cursor = None
    # 定义类方法
    @classmethod
    # 链接数据库并创建表Table  通过参数fieldItems获取字段的数量
    def createDBAndTable(cls,fieldItems,tableName):
        cls.con = sqlite3.connect('DB_all')
        cls.cursor = cls.con.cursor()
        # 拼接游标需要执行的命令
        command = 'create table if not exists {}('.format(tableName)
        tail = ''
        # 字段名为info1-info...
        for fieldItem in range(1,fieldItems+1):
            if fieldItem !=fieldItems:
                tail += 'info{} text,'.format(fieldItem)
            else:
                tail += 'info{} text'.format(fieldItem)
        command +=tail+')'
        # print(command)
        # 创建表
        cls.cursor.execute('{}'.format(command))
    @classmethod
    def closeDB(cls):
        cls.cursor.close()
        cls.con.close()

    @classmethod
    # 添加数据到数据库
    def insertIntoDB(cls,data,tableName):
        # 获取数据元素个数
        length = len(data)
        cls.con = sqlite3.connect('DB_all')
        cls.cursor = cls.con.cursor()
        # 拼接命令
        command = 'insert into {} VALUES ('.format(tableName)
        for i in range(length):
            if i !=length-1:
                command += '"{}",'.format(data[i])
            else:
                command += '"{}")'.format(data[i])

        cls.cursor.execute('{}'.format(command))
        cls.con.commit()


class Spider(object):

    def __init__(self):
        # 实例化对象作为属性 用于操作数据库
        self.dbOpertion = DBManager()
        self.tableName = ''
    #  通过url获取响应的数据code 以及表名tableName
    def getCodeFromUrl(self,url):
        # pattern = re.compile(r'https://www.(.*?).c.*?')
        # self.tableName = pattern.findall(url)[0]
        self.tableName = url.split('.')[1]

        request = Request(url,headers=headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('获取失败')
            return None
        else:
            return code
    # 通过响应的数据code和正则获取目标信息info并返回
    def getInfoAndItemFromCode(self,code,zhengze):
        pattern = re.compile(r'{}'.format(zhengze),re.S)
        info = pattern.findall(code)
        print(info)
        if type(info[0]) == str:
            new_info  = []

            for var in info:
                var_list = []
                var_list.append(var)
            new_info.append(var_list)
            return new_info
        else:
            return info
        # if info:
        #     fieldItems = len(info[0])
        #     self.dbOpertion.createDBAndTable(fieldItems,self.tableName)
        #     for index in info:
        #             self.dbOpertion.insertIntoDB(index,self.tableName)
        #     return info,fieldItems
    # 通过返回的info插入数据
    def insertDBFromInfo(self,info):
        # 获取每个元组的长度
        fieldItems = len(info[0])
        self.dbOpertion.createDBAndTable(fieldItems,self.tableName)
        for index in info:
                self.dbOpertion.insertIntoDB(index,self.tableName)
        self.dbOpertion.closeDB()
        return info


patternDict = {
    'https://www.jd.com/allSort.aspx':'<div.*?<dt>.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>',
    'https://www.qiushibaike.com/hot/page/1':'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',
    'http://www.xiaomi.cn/':'<li onclick="_hmt.push.*?<a.*?alt="(.*?)".*?>.*?<p>.*?"(.*?)".*?</p>'
}

spider = Spider()
for u,p in patternDict.items():
    pattern = p
    code = spider.getCodeFromUrl(u)
    info= spider.getInfoAndItemFromCode(code,pattern)
    spider.insertDBFromInfo(info)




