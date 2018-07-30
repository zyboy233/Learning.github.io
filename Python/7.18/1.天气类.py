import sqlite3
from urllib.request import urlopen
import json,string
from urllib.parse import quote
from xpinyin import Pinyin

p = Pinyin()

class Weather(object):
    def __init__(self,cityList = []):
        self.day = ""
        self.high = ""
        self.low = ""
        self.cityList = cityList
        self.con = None
        self.cursor = None

    def getAllInfo(self):
        # 创建打开数据库
        self.openDB()

        for city in self.cityList:
            cityName = p.get_pinyin(city).replace('-','')
            self.cursor.execute('create table if not exists "{}" (day text,high text,low text)'.format(cityName))
            self.con.commit()

            url = 'https://www.apiopen.top/weatherApi?city={}'.format(city)
            # 获取响应对象
            reponse = urlopen(quote(url,safe=string.printable))
            # 获取响应对象的文本内容
            reponseStr = reponse.read()
            # 将文本转换为字典
            reponseDic = json.loads(reponseStr)

            # 添加昨天数据
            self.cursor.execute('insert into "{}" values("{}","{}","{}")'.format(cityName,reponseDic['data']['yesterday']['date'],reponseDic['data']['yesterday']['high'],reponseDic['data']['yesterday']['low']))
            self.con.commit()
            # 添加今天和以后数据
            for other in reponseDic['data']['forecast']:
                self.cursor.execute('insert into "{}" VALUES ("{}","{}","{}")'.format(cityName,other['date'],other['high'],other['low']))
                self.con.commit()
        self.closeDB()
    def getInfoWith(self,info):

        info['city'] = p.get_pinyin(info['city']).replace('-','')
        self.openDB()
        self.cursor.execute('select * from "{}" WHERE day LIKE "%{}%"'.format(info['city'],info['time']))
        self.con.commit()
        result = self.cursor.fetchall()
        if result:
            print(result)
        else:
            print('暂无相关信息')
    def openDB(self):
        self.con = sqlite3.connect('WeatherDB')
        self.cursor = self.con.cursor()
    def closeDB(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()
w = Weather(['郑州','洛阳','开封','南阳','商丘','驻马店','周口','平顶山'])
# w.getAllInfo()

dic = {}
dic['city'] = input("你想查询哪个城市:")
dic['time'] = input('你想查询哪一天:')

w.getInfoWith(dic)