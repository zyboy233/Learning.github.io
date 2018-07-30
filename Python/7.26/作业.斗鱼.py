# 2.斗鱼直播网站   爬取  “分类“ 页面的全部图片和名字
# 爬取“游戏”页面的全部图片和名字 存入excel

from urllib.request import urlopen,urlretrieve,Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import os
import xlwt


class DYcategory(object):
    def __init__(self):
        self.base_url = 'https://www.douyu.com/directory'
        self.game_url = 'https://www.douyu.com/g_jdqs'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    def spider(self):
        code = self.get_code_with_url(self.base_url)
        self.get_data_with_code(code)
        gamecode = self.get_code_with_url(self.game_url)
        self.get_gamedata_with_code(gamecode)
    def get_data_with_code(self,code):
        soup = BeautifulSoup(code,'lxml')
        imgs = soup.select('#live-list-contentbox li img')
        titles = soup.select('#live-list-contentbox li p')
        # print(img,title)
        try:
            os.mkdir('D:/category')
        except Exception as e:
            print('文件夹已存在:',e)
        finally:
            os.chdir('D:/category')
            for img,title in zip(imgs,titles):
                img = img.get('data-original')
                title = title.get_text()
                # print(img,title)
                urlretrieve(img,title+'.jpg')

    def get_code_with_url(self,url):
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        code = response.read().decode()
        print(code)
        return code
    def get_gamedata_with_code(self,code):
        soup = BeautifulSoup(code,'lxml')
        imgs = soup.select('#live-list-contentbox  a img')
        tittles = soup.select('.play-list-link')
        workBook = xlwt.Workbook(encoding='utf-8')
        sheet = workBook.add_sheet('sheet1')
        try:
            os.mkdir('d:/gamedir')
        except Exception as e:
            print('创建失败:',e)
        finally:
            index = 0
            os.chdir('d:/gamedir')
            for img,title in zip(imgs,tittles):
                img = img.get('data-original')
                title = title.get('title')
                print(img,title)
                urlretrieve(img,title+'.jpg')
                sheet.write(index,0,title)
                sheet.write(index,1,img)
                index+=1
            workBook.save('douyu.xls')

category = DYcategory()
category.spider()