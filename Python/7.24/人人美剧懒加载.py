
# http://www.zimuzu.io/article
from urllib.request import Request,urlopen
import re

class Zimuzu(object):
    def __init__(self):
        self.base_url = 'http://www.zimuzu.io/article/?page='
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.first_page = 1
        self.total_page = 1
    def spider(self):
        code = self.get_code_from_url(self.first_page)
        self.total_page = self.get_total_page(code)
        self.get_data_from_code(code)
        self.get_page_step()
    def get_page_step(self):
        index = 1
        while True:
            signal = input('回车翻页,按E退出')
            if signal !="E":
                code = self.get_code_from_url(index)
                data = self.get_data_from_code(code)
                index += 1
                print(data)
            else:
                break


    def get_data_from_code(self,code):
        pattern = re.compile(r'<li class="clearfix".*?<span.*?>(.*?)</span>.*?<a.*?>(.*?)</a>.*?<p>(.*?)<font.*?>',re.S)
        data = pattern.findall(code)
        return data

    def get_total_page(self,code):
        pattern = re.compile(r'<div class="pages pages-padding">.*?<b>.*?</b>.*?</a>.*?<a href=.*?page=(.*?)>.*?<span>',re.S)
        result = pattern.findall(code)
        result = result[0][0:-1]
        return (int(result))
    def get_code_from_url(self,indexPage):
        url = self.base_url + str(indexPage)
        request = Request(url ,headers=self.headers)
        response = urlopen(request)
        code = response.read().decode()
        return code


z = Zimuzu()
z.spider()