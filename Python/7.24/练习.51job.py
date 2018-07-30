# 练习
# 51job
# 爬取任意城市的python岗位
# 包含公司名称
# 存入execl中


#https://search.51job.com/list/020000%252C030200,000000,0000,00,9,99,python,2,1.html

from urllib.request import Request,urlopen
from urllib.parse import quote
import re
import string,json
import xlwt

class job_51(object):
    def __init__(self,cityList,job):
        self.cityList = cityList
        self.job = job

        self.cityName = ''
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.first_page = 1
        self.total_page = 1
        for city in cityList:
            cityDigitDict = self.get_cityDigit()
            if city == cityList[-1]:
                self.cityName += cityDigitDict[city]
            else:
                self.cityName += cityDigitDict[city] + '%252C'
            # print(self.cityName)
    def get_cityDigit(self):
        url = 'https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20180319='
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        code = response.read().decode('gbk')
        # print(code)
        pattern = re.compile(r'area=(.*?);',re.S)
        result = pattern.findall(code)
        result = json.loads(result[0])
        dict = {}
        for key,value in result.items():
            key = key.strip('\r')
            key = key.strip('\n')
            dict[value] = key
        return dict

    def get_total_page(self,code):
        pattern = re.compile(r'<span class="td">共(.*?)页.*?</span>',re.S)
        result = pattern.findall(code)
        return (int(result[0]))
    def spider(self):
        code = self.get_code_from_url(self.first_page)
        # print(code)
        self.total_page = self.get_total_page(code)

        sheet,workBook = self.openExeclBook()

        record = 1

        for index in range(1,self.total_page+1):
            code = self.get_code_from_url(index)
            dataList = self.get_total_data(code)

            for index in dataList:
                sheet.write(record,0,index[0])
                sheet.write(record,1,index[1])
                sheet.write(record,2,index[2])
                sheet.write(record,3,index[3])
                sheet.write(record,4,index[4])
                record +=1
        workBook.save('python职位介绍表.xls')


    def get_total_data(self,code):
        pattern = re.compile(r'<div class="el".*?<span.*?<a target.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<span class.*?>(.*?)</span>.*?<span class.*?>(.*?)</span>.*?<span class.*?>(.*?)</span>',re.S)
        pattern_space = re.compile(r'\s', re.S)
        result = pattern.findall(code)
        list = []
        for job, company, add, salary, time in result:
            job = job.strip('\r\n')
            job = re.sub(pattern_space, '', job)
            list.append([job, company, add, salary, time])
        return list

    def openExeclBook(self):
        workBook = xlwt.Workbook(encoding='utf-8')
        sheet = workBook.add_sheet('python职位表_51job')
        sheet.write(0,0,'职位名')
        sheet.write(0,1,'公司名')
        sheet.write(0,2,'工作地点')
        sheet.write(0,3,'薪资')
        sheet.write(0,4,'发布时间')

        return sheet, workBook
    def get_code_from_url(self,indexPage):
        url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html'.format(self.cityName,self.job,indexPage)
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        code = response.read().decode('gbk')
        return code
cityList = []

while True:
    city = input('请输入你要查询的城市,按E退出:')
    if city == 'E':
        break
    cityList.append(city)
job = input('请输入你要查询的职位:')

spider = job_51(cityList,job)
spider.spider()