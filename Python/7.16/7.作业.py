# 游客和导游
# 导游查询旅游信息 ，提取指定字段到数据库
# 根据游客的时间 推荐不同天数的旅游项目
# 要求：按照今天的数据库重构方式来实现
# 北京 杭州 上海  郑州  洛阳
# http://api.map.baidu.com/telematics/v3/travel_city?location=北京&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json

from urllib.request import urlopen
from urllib.parse import quote
import string,json
from prettyprinter import pprint
import sqlite3
class Data(object):
    def __init__(self,city = '',day = '',des = '',addr = ''):
        self.city = city
        self.day = day
        self.des = des
        self.addr = addr
class DBOperation(object):
    def __init__(self,dbName= '',tableName = ''):
        self.dbName = dbName
        self.tableName = tableName
        self.con = None
        self.cursor = None
    def createDBAndTable(self):
        self.con = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists "{}"(city text,day text,des text,addr text)'.format(self.tableName))
    def commitAndClose(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()
    def openDB(self):
        self.con = sqlite3.connect('DBTourism')
        self.cursor = self.con.cursor()
    def addToDBTourism(self,data):
        self.openDB()
        self.cursor.execute('INSERT into "{}" values ("{}","{}","{}","{}")'.format(self.tableName,data.city,data.day,data.des,data.addr))
        self.commitAndClose()
    def selectDBTourism(self,city,day):
        self.openDB()
        self.cursor.execute('select * from "{}" WHERE city = "{}" AND day = "{}"'.format(self.tableName,city,day))
        result = self.cursor.fetchall()
        self.commitAndClose()
        print(result)
class Guidance(DBOperation):
    def __init__(self,dbName='',tableName=''):
        super(Guidance, self).__init__(dbName,tableName)
    def datalist(self,cityName):
        list1 = []
        list2 = []
        url = 'http://api.map.baidu.com/telematics/v3/travel_city?location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(
            cityName)
        response = urlopen(quote(url, safe=string.printable))
        responseData = response.read()
        # print(responseData)
        responseJson = json.loads(responseData)
        # print(responseJson)
        for index in responseJson['result']['itineraries']:
            list2 = []
            list2.append(index['name'])
            list2.append(index['description'])
            for dic in index['itineraries']:
                for dic1 in dic['path']:
                    list2.append(dic1['name'])
            list1.append(list2)
        return list1
    def Introduce(self,tourist):
        dict = {1:'一日游',2:'二日游',3:'三日游',5:'五日游',6:'六日游'}
        result = super(Guidance,self).selectDBTourism(tourist.city,dict[tourist.days])
        print(result)
class Tourist(object):
    def __init__(self,city,days):
        self.city = city
        self.days = days
g = Guidance('DBTourism','tableTour')
g.createDBAndTable()
# cityList = ["北京","杭州","上海","郑州","洛阳"]
# for city in cityList:
#     list = g.datalist(city)
#     print(list)
#     for i in list:
#         char = ''
#         for j in i[2:]:
#             char +=j+' '
#         d = Data(city,i[0],i[1],char)
#         g.addToDBTourism(d)
t = Tourist('上海',2)
g.Introduce(t)


