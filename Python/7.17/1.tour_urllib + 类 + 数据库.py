
# 游客和导游
# 导游查询旅游信息 ，提取指定字段到数据库
# 根据游客的时间 推荐不同天数的旅游项目
# 要求：按照今天的数据库重构方式来实现
# 北京 杭州 上海  郑州  洛阳
# url http://api.map.baidu.com/telematics/v3/travel_city?location=北京&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json

from urllib.request import urlopen
from urllib.parse import quote
import string,json
import sqlite3
from xpinyin import Pinyin

class DaoYou(object):
    def __init__(self,dbName = '',cityList = []):
        self.cityList = cityList
        self.dbName = dbName
        # 不知道值是什么 但是知道值是什么类型
        self.tableName = ''
        # 不知道值是什么 也不知道值是什么类型
        self.con = None
        self.cursor = None

    def getAllCityInfo(self):
        self.con = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.con.cursor()

        for city in self.cityList:
            p = Pinyin()
            self.tableName = p.get_pinyin(city)
            self.tableName = self.tableName.replace('-','')
            self.cursor.execute('create table if not exists "{}"(name text,description text,areaName list)'.format(self.tableName))
            self.con.commit()

            url = 'http://api.map.baidu.com/telematics/v3/travel_city?location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
            #UnicodeEncodeError: 'ascii' codec can't encode characters in position 39-40: ordinal not in range(128)
            #编码错误
            #url 不支持中英混写 报错
            # reponse = urlopen(url)
            # safe = string.printable 使用安全转码
            # 只让中文进行转码 但是特殊字符保留
            response = urlopen(quote(url,safe=string.printable))
            # 读取地址里面的数据 返回的永远是是字符串
            responseStr = response.read()
            # print(responseStr)
            # 将字符串转换成字典
            responseDic = json.loads(responseStr)
            # print(responseDic)
            for day in responseDic['result']['itineraries']:
                name = day['name']
                des = day['description']
                areaName = []
                # print(day['description'])
                for time in day['itineraries']:
                    for value in time['path']:
                        # print(value['name'])
                        areaName.append(value['name'])
                self.cursor.execute('insert into "{}" VALUES ("{}","{}","{}")'.format(self.tableName,name,des,areaName))
                self.con.commit()

    def getInfoWith(self,youke):
        p = Pinyin()
        dayList = ['一','二','三','四','五','六','七']

        youke.time = dayList[int(youke.time)-1] + '日游'

        youke.city = (p.get_pinyin(youke.city)).replace('-','')

        self.con = sqlite3.connect('{}'.format(self.dbName))

        self.cursor = self.con.cursor()

        self.cursor.execute('select * from "{}" WHERE name = "{}"'.format(youke.city,youke.time))

        self.con.commit()
        result = self.cursor.fetchall()
        if result == 0:
            print('抱歉,目前该城市暂无{}计划'.format(youke.city))
        else:
            print(result)
class YouKe(object):
    def __init__(self,city = '',time = ''):
        self.city = city
        self.time = time
dao = DaoYou('cityDB',['北京','上海','杭州','郑州','洛阳'])
print(dao.cityList)
# print(dao.getAllCityInfo())

youke = YouKe()
youke.city = input('你想去哪个城市旅游:')
youke.time = input('你有几天的时间:')

dao.getInfoWith(youke)
