import requests,os
from lxml import etree
from urllib.request import urlopen,Request
from urllib.request import urlretrieve,ProxyHandler
from fake_useragent import UserAgent
import threading

class Meizitu(object):
    def __init__(self):
        self.base_url = 'http://www.mmjpg.com'
        self.headers = UserAgent()
        self.record = 1


    def spider(self):
        self.get_data_with_url('/home/19')
    def get_data_with_url(self,url=''):
        headers = {
            'User-Agent':self.headers.random
        }
        url = self.base_url + url
        response = requests.get(url,headers=headers).content
        code = etree.HTML(response)
        items = code.xpath('//div[@class="pic"]/ul/li')
        print(items)
        for item in items:
            item_url = item.xpath('.//a/@href')[0]
            item_name = item.xpath('.//a/img/@alt')[0]
            # print(item_url,item_name)
            self.record = 1
            try:
                os.mkdir('D:/meizitu/{}'.format(item_name))
                os.chdir('D:/meizitu/{}'.format(item_name))
                print(item_url+'  正在下载本篇...')
                self.get_sub_data_with_url(item_url)
            except Exception as e:
                print('文件夹创建失败',e)
            finally:
                os.chdir(os.path.pardir)
        next_page = code.xpath('//div[@class="page"]/a[last()-1]/@href')[0]
        print('http://www.mmjpg.com' + next_page)

        self.get_data_with_url(next_page)

    def get_sub_data_with_url(self,url):
        headers = {
            'User-Agent':self.headers.random,
            'referer':'{}/1'.format(url)
        }
        response = requests.get(url,headers=headers).content
        code = etree.HTML(response)
        jpg = code.xpath('//div[@class="content"]/a/img/@src')[0]
        request = Request(jpg,headers=headers)
        jpg = urlopen(request).read()
        with open('{}.jpg'.format(self.record),'wb')as j:
            j.write(jpg)
            j.close()
        self.record += 1
        next_page = code.xpath('//div[@class="page"]/a[last()]/@href')[0]
        next_article = code.xpath('//div[@class="page"]/a[last()]/text()')[0]
        if next_article == '下一篇':
            print('这一篇没了')
            return
        self.get_sub_data_with_url(self.base_url+next_page)
meizitu = Meizitu()
meizitu.spider()