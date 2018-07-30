import xlwt
import requests
from lxml import etree
from fake_useragent import UserAgent

class DBMovie(object):
    def __init__(self):
        self.base_url = 'http://movie.douban.com/top250'
        self.current_page = 1
        self.headers = UserAgent()
        self.workBook = None
        self.sheet = None
    def start_load_movie(self):
        self.get_excel()
        # 第一次调用该方法 url值可以不用传
        self.get_code_with_url()
        self.workBook.save('豆瓣top250.xls')
    def get_excel(self):
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('电影排行榜')
        self.sheet.write(0,0,'排名')
        self.sheet.write(0,1,'影片')
        self.sheet.write(0,2,'导演和演员')
        self.sheet.write(0,3,'评分')
        self.sheet.write(0,4,'评论人次')
        self.record = 1
    def get_code_with_url(self,url=''):
        headers = {
            'User-Agent':self.headers.random
        }
        full_url = self.base_url + url
        response = requests.get(full_url,headers=headers).text
        # print(response)
        code = etree.HTML(response)
        item_div = code.xpath('//div[@class="item"]')
        # print(item_div)
        for tag in item_div:
            # .从当前节点开始取
            # ..从父节点开始取
            rank = tag.xpath('.//em[@class=""]/text()')[0]
            movie_name = tag.xpath('.//div[@class="hd"]/a/span/text()')
            name = ''
            for movie in movie_name:
                name += movie
            director = tag.xpath('.//div[@class="bd"]/p[@class=""]/text()')[0]
            director = director.strip('\n').replace(' ','')
            star = tag.xpath('.//span[@class="rating_num"]/text()')[0]
            comment_num = tag.xpath('.//div[@class="star"]/span[last()]/text()')[0]
            comment_num = comment_num[0:-3]
            # print(rank,name,director,star,comment_num)
            self.sheet.write(self.record,0,rank)
            self.sheet.write(self.record,1,name)
            self.sheet.write(self.record,2,director)
            self.sheet.write(self.record,3,star)
            self.sheet.write(self.record,4,comment_num)
            self.record += 1
        self.get_next_page(code)
    def get_next_page(self,code):
        next_url = code.xpath('//span[@class="next"]/a/@href')
        if len(next_url) == 0:
            print('已经是最后一页了')
            return
        self.get_code_with_url(next_url[0])
movie = DBMovie()
movie.start_load_movie()