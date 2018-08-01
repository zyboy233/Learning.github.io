from urllib.request import Request,urlopen
from lxml import etree
from fake_useragent import UserAgent
import xlwt

class Kuan(object):
    def __init__(self):
        self.base_url = 'https://www.coolapk.com/apk?p=1'
        self.headers = UserAgent()
        self.workBook = None
        self.sheet = None
        self.record = 1
        self.page = 1
    def spider(self):
        self.createWorkBook()
        self.get_code_with_url(self.base_url)
        self.workBook.save('D:/酷安.xls')
    def get_code_with_url(self,url):
        print('正在爬取酷安app第{}页...'.format(self.page))
        headers = {
            'User-Agent':self.headers.random
        }
        print(headers)
        request = Request(url,headers=headers)
        response = urlopen(request).read().decode()
        # print(response)
        code = etree.HTML(response)
        items = code.xpath('//div[@class="app_left_list"]/a')
        for item in items:
            title = item.xpath('.//p[@class="list_app_title"]/text()')[0]
            info = item.xpath('.//p[@class="list_app_info"]//text()')
            grade = info[0].split(' ')[0]
            large = info[0].split(' ')[2]
            download = info[1].split(' ')[0]
            status = info[1].split(' ')[2]
            # print(grade,large,download,status)
            des = item.xpath('.//p[@class="list_app_description"]/text()')
            if len(des) == 0:
                des = ''
            else:
                des = des[0]
            list = [title,grade,large,download,status,des]
            for index,item in enumerate(list):
                self.sheet.write(self.record,index,item)
            self.record += 1
        self.page += 1
        self.next_page(code)
    def next_page(self,code):
        next_page_url = code.xpath('//ul[@class="pagination"]/li[last()-1]/a/@href')[0]
        if next_page_url == 'javascript:void(0);':
            print('已经到最后一页了')
            return
        if next_page_url == '/apk?p=20':
            return
        self.get_code_with_url('https://www.coolapk.com'+next_page_url)
    def createWorkBook(self):
        list = ['应用名称','评分','大小','下载量','更新状态','应用简介']
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('app')
        for index,item in enumerate(list):
            self.sheet.write(0,index,item)


kuan = Kuan()
kuan.spider()