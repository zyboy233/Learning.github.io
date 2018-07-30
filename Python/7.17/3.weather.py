
# url : https://www.apiopen.top/weatherApi?city=郑州
import sqlite3
from urllib.request import urlopen
from urllib.parse import quote
import string,json
from xpinyin import Pinyin

class Weather(object):
    def __init__(self,dbName = ''):
        self.dbName = dbName
        self.tableName = ''
        self.con = None
        self.cursor = None
        self.con = sqlite3.connect(self.dbName)
        self.cursor = self.con.cursor()
    def addWeather(self,cityList):

        for city in cityList:
            url = 'https://www.apiopen.top/weatherApi?city={}'.format(city)
            response = urlopen(quote(url,safe=string.printable))
            responseStr = response.read()
            responseJson = json.loads(responseStr)
            print(responseJson)

            p = Pinyin()
            city = p.get_pinyin(city)
            city = city.replace('-','')
            self.cursor.execute('create table if not exists {}(date text,high text,low text)'.format(city))
            self.con.commit()
            list = []
            list.append(responseJson['data']['yesterday']['date'])
            list.append(responseJson['data']['yesterday']['high'])
            list.append(responseJson['data']['yesterday']['low'])
            self.cursor.execute('INSERT INTO {} VALUES ("{}","{}","{}")'.format(city, list[0], list[1], list[2]))
            self.con.commit()
            for index in responseJson['data']['forecast']:
                list = []
                list.append(index['date'])
                list.append((index['high']))
                list.append(index['low'])
                self.cursor.execute('INSERT INTO {} VALUES ("{}","{}","{}")'.format(city,list[0],list[1],list[2]))
                self.con.commit()


    def selectWeather(self):
        print("""
        查询天气信息:城市名(例:洛阳),日期(例:星期一)
        """)
        city = input('请输入你要查询的城市:')
        day = input('请输入你要查询的日期:')
        p = Pinyin()
        city = p.get_pinyin(city)
        city = city.replace('-','')
        self.cursor.execute('select * from {} WHERE date LIKE "%{}%"'.format(city,day))
        self.con.commit()
        result = self.cursor.fetchall()
        if result == 0:
            print('您输入的城市或者日期有误')
        else:
            print(result)
        self.cursor.close()
        self.con.commit()
city = ['洛阳','开封','南阳','商丘','信阳','驻马店','周口']
w = Weather('dbWeathers')
# w.addWeather(city)
w.selectWeather()


