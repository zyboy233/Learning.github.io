from urllib.request import Request,urlopen
from lxml import etree
import xlwt
class Zimuzu(object):
    def __init__(self):
        self.base_url = 'http://www.zimuzu.io/resourcelist'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.workBook = None
        self.sheet = None
        self.record = 1
    def spider(self):
        self.create_workBook()
        self.get_data_with_url(self.base_url)
        self.workBook.save('人人影视库.xls')
    def get_data_with_url(self,url):
        request = Request(url,headers=self.headers)
        response = urlopen(request).read()

        code = etree.HTML(response)
        items = code.xpath('//div[@class="resource-showlist has-point"]/ul/li[@class="clearfix"]')
        print(items)
        for item in items:
            point = item.xpath('.//span[@class="point"]//text()')
            if len(point) == 2:
                point = point[0] + point [1]
            point = ''
            type = item.xpath('.//h3[@class="f14"]/a/strong/text()')
            if len(type) == 0:
                type = ''
            type = type[0]
            name = item.xpath('.//h3[@class="f14"]/a/text()')[0]
            num = item.xpath('.//h3[@class="f14"]/font[@class="f4"]/text()')
            if len(num)==0:
                num = ''
            num = num[0]
            try:
                self.sheet.write(self.record,0,point)
                self.sheet.write(self.record,1,type)
                self.sheet.write(self.record,2,name)
                self.sheet.write(self.record,3,num)
            except Exception as e:
                print('写入失败',e)
            finally:
                self.record += 1
        self.next_page_with_code(code)
    def next_page_with_code(self,code):
        next_page = code.xpath('//div[@class="pages"]/div/a[last()-1]/@href')
        print(next_page)
        if len(next_page) == 0:
            print('获取完毕')
            return
        self.get_data_with_url('http://www.zimuzu.io'+ next_page[0])
    def create_workBook(self):
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('movies')
        self.sheet.write(0,0,'影视评分')
        self.sheet.write(0,1,'影视类型')
        self.sheet.write(0,2,'影视名称')
        self.sheet.write(0,3,'更新进度')


zimuzu = Zimuzu()
zimuzu.spider()