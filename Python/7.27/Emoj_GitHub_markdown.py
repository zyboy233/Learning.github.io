import requests,os
from urllib.request import urlretrieve
from lxml import etree
import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

class Emoj(object):
    def __init__(self):
        self.base_url = 'https://www.webpagefx.com/tools/emoji-cheat-sheet/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            ,'Host':'www.webpagefx.com'
        }
    def spider(self):
        self.get_data_with_url(self.base_url)
    def get_data_with_url(self,url):
        response = requests.get(url,verify=False).text
        code = etree.HTML(response)
        print(code)
        jpgs = code.xpath('//ul[@id="emoji-people"]/li/div/span[@class="emoji"]')
        names = code.xpath('//ul[@id="emoji-people"]/li/div/span[@class="name"]/text()')
        os.chdir('D:/Emoj')
        for jpg,name in zip(jpgs,names):
            jpg = jpg.xpath('@data-src')[0]
            url = self.base_url+jpg
            print(url)
            urlretrieve(self.base_url+jpg,name+'.png')

emoj = Emoj()
emoj.spider()