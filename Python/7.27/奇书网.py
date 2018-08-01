# 作业：奇书网 ，玄幻奇幻类小说
# 将小说名，点击次数，文件大小，书籍类型。更新日期，连载状态。
# 书籍作者，小说简介，下载地址存储到excel里面

import xlwt
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup

class Qishu(object):
    def __init__(self):
        self.base_url = 'https://www.qisuu.la/soft/sort01/index_1.html'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.workBook = None
        self.sheet = None
        self.record = 1

    # 主爬虫程序
    def spider(self):
        self.create_workBook()
        self.get_data_with_url(self.base_url)
        # 创建excle工作簿
        self.workBook.save('奇书小说.xls')

    # 请求url获取信息
    def get_data_with_url(self,url):
        print('正在获取:{} ...'.format(url))
        # 请求url
        request = Request(url, headers=self.headers)
        try:
            response = urlopen(request).read()
        except Exception as e:
            print('请求本页失败',e)
            print('重新获取本页:{}...'.format(url))
            self.get_data_with_url(url)
        # print(response)
        soup = BeautifulSoup(response,'lxml')

        # 分支语句判断能否获取本页tspage,获取不到时
        # 重新获取
        tspage = soup.select('.tspage a')
        if len(tspage) == 0:
            print('重新获取本页:{}'.format(url))
            self.get_data_with_url(url)
        else:
            # 获取一页中的所有小说条目
            items = soup.select('.listBox ul li')
            for item in items:
                # find获取每个条目中的第一个url链接即小说详情
                url = item.find('a').get('href')
                # print(url)
                # 获取详情页信息-----------------------------------------
                self.get_sub_data_with_url('https://www.qisuu.la' + url)
            # 获取下一页url
            try:
                tspage = soup.select('.tspage a')
                if tspage[-2].get_text() != '下一页' :
                    print('没有下一页了,亲...')
                    return
                next_page = tspage[-2].get('href')
                page_url = 'https://www.qisuu.la'+next_page
                # print(page_url)
                # 传递下一页url 回调函数
                self.get_data_with_url(page_url)
            except Exception as e:
                print('获取失败:',e)
    # 详情页
    def get_sub_data_with_url(self,url):
        request = Request(url, headers=self.headers)
        response = urlopen(request).read()
        print(response.decode())
        soup = BeautifulSoup(response, 'lxml')

        # 获取指定信息
        name = soup.select('.detail_right h1')[0].get_text()
        infos = soup.select('.detail_right ul .small')
        list = [name]
        for index in range(0,6):
            # 取文本并处理数据
            option = infos[index].get_text().split('：')[1]
            list.append(option)
        show = soup.select('.showInfo p')[0].get_text()
        url = soup.select('.showDown ul li script')[0].get_text().split("'")[3]
        list.append(show)
        list.append(url)

        # 写入excel表
        for index,option in enumerate(list):
            self.sheet.write(self.record,index,option)
        # record 控制插入位置
        self.record += 1

    # 创建excel工作簿
    def create_workBook(self):
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('小说')
        # 插入头信息
        for index,option in enumerate(['小说名称','点击次数','文件大小','书籍类型','更新日期','连载状态','书籍作者','小说简介','下载地址']):
            self.sheet.write(0,index,option)

# 实例化对象
qishu = Qishu()
qishu.spider()