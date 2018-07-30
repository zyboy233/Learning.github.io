from urllib.request import urlopen,Request
from urllib.parse import quote
import re
import string

# 处理excel的模块
import xlwt

# https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%83%91%E5%B7%9E%2B%E5%8E%A6%E9%97%A8&kw=python&sm=0&p=1
# 目的:1.爬取数据 2.存储到excel中

class ZLZP(object):
    def __init__(self,cityList = [],workName = ''):
        self.cityList = cityList
        self.workName = workName
        self.baseUrl = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        self.cityString = ''
        self.currentIndex  = 1
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
        self.total_page = 1
        for cityName in self.cityList:
            if cityName == self.cityList[-1]:
                self.cityString += quote(cityName)
            else:
                self.cityString += quote(cityName)
                self.cityString += '%2B'
    def start_spider(self):
        # 第一次调用传值1
        # 获取第一个网页的源码  目的:得到总页数(信息数 / 每页显示的条数)
        code = self.get_code_with_url(1)
        print(code)
        self.get_total_page(code)
        # 创建一个execl对象 设置编码格式 标题 sheet
        sheet , workBook = self.open_execl_file()
        # 记录写入的行数 目的:让后来的数据插入到之前数据的后方
        record_row = 1
        # 获取每一页的数据
        for index in range(1 , self.total_page + 1):
            # 分别获取每一页的源码
            code = self.get_code_with_url(index)
            if code == None:
                continue
            # 分别剥离每一页的数据 [[],[],[],...]
            result_list = self.get_all_data(code)
            # 获取具体每一条数据
            for job,company,salary,location in result_list:
                sheet.write(record_row,0,job)
                sheet.write(record_row,1,company)
                sheet.write(record_row,2,salary)
                sheet.write(record_row,3,location)
                record_row += 1
        workBook.save('python职位介绍表.xls')
    def get_all_data(self,code):
        pattern = re.compile(r'<table.*?class="newlist".*?>.*?<td class="zwmc".*?>.*?<a.*?>(.*?)</a>.*?<td class="gsmc">.*?<a.*?>(.*?)</a>.*?<td class="zwyx">(.*?)</td>.*?<td class="gzdd">(.*?)</td>', re.S)
        result = pattern.findall(code)
        # print(result)
        list = []
        for value in result:
            jobName = value[0]
            companyName = value[1]
            salary = value[2]
            location = value[3]

            pattern = re.compile(r'<.*?>',re.S)
            jobName = re.sub(pattern,'',jobName)
            companyName = re.sub(pattern,'',companyName)
            list.append([jobName,companyName,salary,location])
        # print(list)
        return list
    # 创建execl
    def open_execl_file(self):
        # 创建工作表对象  并设置编码方方式为utf-8
        workBook = xlwt.Workbook(encoding='utf-8')
        # 新增sheet
        sheet = workBook.add_sheet('python职位表')
        # 值1:行 索引0开始
        # 值2:列 索引0开始
        # 值3:标题
        sheet.write(0 , 0 , '职位名称')
        sheet.write(0 , 1 , '公司名称')
        sheet.write(0 , 2 , '薪资水平')
        sheet.write(0 , 3 , '工作地点')
        return sheet,workBook
    def get_total_page(self,code):
        # pattern = re.compile(r'<table.*?class="newlist".*?>.*?<td class="zwmc".*?>.*?<a.*?>(.*?)&',re.S)
        pattern = re.compile(r'<span class="search_yx_tj">.*?<em>(.*?)</em>',re.S)
        result = pattern.findall(code)
        print(result)
        num = int(result[0])
        if num:
            if num % 60 == 0:
                self.total_page = num // 60
            else:
                self.total_page = num // 60 +1
                print(self.total_page)
    def get_code_with_url(self,pageIndex):
        full_url = self.baseUrl + 'jl=' + self.cityString + '&kw=' + self.workName + '&p=' + str(pageIndex)
        print(full_url)
        request = Request(full_url,headers=self.headers)
        try:
            response = urlopen(request)
            code = response.read().decode()
        except Exception as e :
            print('请求失败',e)
        else:
            return code

cityList = []
while True:
    city = input('请输入你想去的城市:')
    if city =="E":
        break
    cityList.append(city)
job = input('请输入你喜欢的工作:')

zp = ZLZP(cityList,job)
zp.start_spider()

