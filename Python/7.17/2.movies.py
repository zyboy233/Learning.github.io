
# url : https://api.douban.com/v2/movie/in_theaters
# url : https://api.douban.com/v2/movie/us_box
import sqlite3
from urllib.request import urlopen
import json

class Movies(object):
    def __init__(self,dbName = ''):
        self.dbName = dbName
        self.tableName = ''
        self.con = None
        self.cursor = None
    def addMovieInfo(self):
        self.con = sqlite3.connect(self.dbName)
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tableMovies(name text,year text,average text,casts list)')
        self.con.commit()

        url = 'https://api.douban.com/v2/movie/in_theaters'
        response = urlopen(url)
        responseStr = response.read()
        # print(responseStr)
        responseJson = json.loads(responseStr)
        responseJson = json.loads(responseStr)
        # print(responseJson)
        for movie in responseJson['subjects']:
            movieList = []
            movieListCasts = []
            movieList.append(movie['title'])
            movieList.append(movie['year'])
            movieList.append(movie['rating']['average'])
            for cast in movie['casts']:
                movieListCasts.append(cast['name'])
            movieList.append(movieListCasts)
            print(movieList)
            self.cursor.execute('INSERT INTO tableMovies VALUES ("{}","{}","{}","{}")'.format(movieList[0],movieList[1],movieList[2],movieList[3]))
            self.con.commit()

        url = 'https://api.douban.com/v2/movie/us_box'
        response = urlopen(url)
        responseStr = response.read()
        # print(responseStr)
        responseJson = json.loads(responseStr)
        responseJson = json.loads(responseStr)
        # print(responseJson)
        self.cursor.execute('CREATE TABLE IF NOT EXISTS ustableMovies(name text,year text,average text,casts list)')
        self.con.commit()
        for index in responseJson['subjects']:
            movieList = []
            castList = []
            movieList.append(index['subject']['title'])
            movieList.append(index['subject']['year'])
            movieList.append(index['subject']['rating']['average'])
            for cast in index['subject']['casts']:
                castList.append(cast['name'])
            movieList.append(castList)
            print(movieList)
            self.cursor.execute('INSERT INTO ustableMovies VALUES ("{}","{}","{}","{}")'.format(movieList[0], movieList[1], movieList[2],movieList[3]))
            self.con.commit()
        self.cursor.close()
        self.con.close()

    def selectMovies(self):
        print("""
        查找电影:(0.国内  1.国外)
        """)
        dic = {'1':'ustableMovies','0':'tableMovies'}
        country = input('请输入国内外对应数字:')
        average = input('请输入评分:')
        self.con = sqlite3.connect(self.dbName)
        self.cursor = self.con.cursor()
        self.cursor.execute('select * from {} WHERE average>={}'.format(dic[country],average))
        result = self.cursor.fetchall()
        print(result)
m = Movies('dbMovies')
# m.addMovieInfo()
m.selectMovies()