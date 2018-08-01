# url = 'https://www.ugirls.com/Models/'

import requests,os
from urllib.request import urlretrieve
from lxml import etree
import xlwt
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

class Emoj(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/hot'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.page = 1
        self.workBook = None
        self.sheet = None
        self.record = 1
    def spider(self):
        self.create_workBook()
        self.get_data_with_url(self.base_url)
        self.workBook.save('D:/糗事百科.xls')
    def get_data_with_url(self,url):
        response = requests.get(url,headers = self.headers).text
        code = etree.HTML(response)
        print(code)
        items = code.xpath('//div[@id="content-left"]/div[contains(@class,artice)]')
        # print(items)
        for item in items:
            user = item.xpath('.//h2/text()')[0]
            content = item.xpath('.//div[@class="content"]/span/text()')[0]
            user = user.strip('\n')
            content = content.replace('\n','')
            print(user)
            print(content)
            self.sheet.write(self.record,0,user)
            self.sheet.write(self.record,1,content)
            self.record += 1
        self.next_page_with_code(code)
    def next_page_with_code(self,code):
        next_page = code.xpath('//ul[@class="pagination"]/li[last()]')[0]
        next_page = next_page.xpath('.//a/@href')
        if next_page[0] == "/week/":
            print('最后一页了...')
            return
        url = 'https://www.qiushibaike.com' + next_page[0]
        self.get_data_with_url(url)
    def create_workBook(self):
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('糗百')
        self.sheet.write(0,0,'用户名:')
        self.sheet.write(0,1,'内容:')
emoj = Emoj()
emoj.spider()