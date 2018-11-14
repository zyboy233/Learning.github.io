import requests,os
from lxml import etree
from urllib.request import urlopen,Request
from urllib.request import urlretrieve,ProxyHandler
# from fake_useragent import UserAgent
import threading
import time
from queue import Queue


class Meizitu(object):
    def __init__(self):
        self.base_url = 'http://www.mmjpg.com'
        # self.headers = UserAgent()
    def spider(self):
        self.get_data_with_url('/home/2')
    def get_data_with_url(self,url=''):
        headers = {
            # 'User-Agent':self.headers.random
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        url = self.base_url + url
        response = requests.get(url,headers=headers).content
        code = etree.HTML(response)
        items = code.xpath('//div[@class="pic"]/ul/li')
        # print(items)
        for item in items:
            item_url = item.xpath('.//a/@href')[0]
            item_name = item.xpath('.//a/img/@alt')[0]
            q_meizi.put({'name':item_name,'url':item_url})
        try:
            next_page = code.xpath('//div[@class="page"]/a[contains(text(), "下一页")]/@href')[0]
        except Exception as e:
            print('获取page失败:',e)
        else:
            print('http://www.mmjpg.com' + next_page)
            self.get_data_with_url(next_page)

class GetJpg(object):
    def __init__(self,lock):
        self.lock = lock
        # self.referer =
    def get_sub_data_with_url(self,url,name):
        print(url)
        headers = {
            # 'User-Agent':self.headers.random,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'referer':'{}'.format(url)
        }
        response = requests.get(url,headers=headers).content
        code = etree.HTML(response)
        try:
            jpg = code.xpath('//div[@class="content"]/a/img/@src')[0]
        except Exception as e:
            print('获取jpg错误: ',e)
            return
        else:
            request = Request(jpg,headers=headers)
            jpg = urlopen(request).read()
            self.lock.acquire()
            if not os.path.exists('D:\meizitu\{}'.format(name)):
                os.mkdir('D:\meizitu\{}'.format(name))
            os.chdir('D:\meizitu\{}'.format(name))
            with open('D:\meizitu\{}\{}.jpg'.format(name,str(time.time())),'wb') as j:
                j.write(jpg)
                j.close()
            self.lock.release()
            next_page = code.xpath('//div[@class="page"]/a[last()]/@href')[0]
            next_article = code.xpath('//div[@class="page"]/a[last()]/text()')[0]
            if next_article == '下一篇':
                print('这一篇没了')
                return
            self.get_sub_data_with_url('http://www.mmjpg.com' + next_page ,name)

q_meizi = Queue()
def start():
    lock = threading.Lock()
    m = Meizitu()
    sub_thread = threading.Thread(target=m.spider, name='spider')
    sub_thread.start()

    num = 0
    while True:
        if (len(threading.enumerate()) == 5):
            continue
        if not q_meizi.empty():
            print('create thread: %s ' % num)
            item = q_meizi.get()
            getjpg = GetJpg(lock)
            sub_thread = threading.Thread(target=getjpg.get_sub_data_with_url,args=(item['url'],item['name']))
            sub_thread.start()
            num += 1

if __name__ == '__main__':
    start()