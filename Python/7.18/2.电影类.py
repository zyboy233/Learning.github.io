# url : https://api.douban.com/v2/movie/in_theaters
# url : https://api.douban.com/v2/movie/us_box
from urllib.request import urlopen
import string,json
import sqlite3
class Movie(object):
    def __init__(self):
        self.con = None
        self.cursor = None
        self.url = ''
    def getHotInfo(self):
        self.con  = sqlite3.connect('movieDB')
        self.cursor = self.con.cursor()


        url = 'https://api.douban.com/v2/movie/in_theaters'

        reponse = urlopen(url)

        reponseStr = reponse.read()

        reponseDic = json.loads(reponseStr)

        print(reponseDic)
        self.cursor.execute('create table if not exists hotTable(title text,average text,year text,castName list)')
        self.con.commit()
        for movieDic in reponseDic['subjects']:
            title = movieDic['title']
            average = movieDic['rating']['average']
            year = movieDic['year']
            castList = []
            for castDic in movieDic['casts']:
                castList.append(castDic['name'])

            self.cursor.execute('insert into hotTable VALUES ("{}","{}","{}","{}")'.format(title,average,year,castList))
            self.con.commit()
    def getMovieWith(self,name):
        self.con = sqlite3.connect('movieDB')
        self.cursor = self.con.cursor()
        self.cursor.execute('select * from hotTable WHERE castName LIKE "%{}%"'.format(name))
        self.con.commit()
        result  = self.cursor.fetchall()
        if result :
            print('为你推荐的电影:{}'.format(result))
        else:
            print('暂无')
m = Movie()
# m.getHotInfo()
m.getMovieWith(input('你喜欢哪个演员的电影:'))
