import requests,os
from lxml import etree
from urllib.request import urlopen,Request

class Meizitu(object):
    def __init__(self):
        self.first_page = 5
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'referer':'http://www.meizitu.com/a/more_1.html'
        }
    def spider(self):
        code = self.get_code_with_url(self.first_page)
        sub_url_list = self.get_sub_url_with_code(code)

        for sub_url in sub_url_list:
            sub_code = self.get_sub_code_with_sub_url(sub_url)
            jpg_url_name_list = sub_code.xpath('//div[@class="metaRight"]/h2/a/text()')
            jpg_url_list = sub_code.xpath('//div[@id="picture"]/p/img/@src')
            if jpg_url_list:
                try:
                    os.makedirs('D:/realmeizitu/{}'.format(jpg_url_name_list[0]))
                except Exception as e:
                    print(e)

                for index,jpg_url in enumerate(jpg_url_list):
                    request = Request(jpg_url,headers=self.headers)
                    response = urlopen(jpg_url).read()
                    with open('D:/realmeizitu/{}/{}.jpg'.format(jpg_url_name_list[0],str(index)),'wb')as j:
                        j.write(response)
                        j.close()
    def get_sub_code_with_sub_url(self,sub_url):
        response = requests.get(sub_url)
        response.encoding = response.apparent_encoding
        root = etree.HTML(response.text)
        return root


    def get_sub_url_with_code(self,code):
        root = etree.HTML(code)
        sub_url_list = root.xpath('//div/h3/a/@href')
        return sub_url_list
    def get_code_with_url(self,indexPage):
        url = 'http://www.meizitu.com/a/more_{}.html'.format(str(indexPage))
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        return response.text
if __name__ == '__main__':
    meizi = Meizitu()
    meizi.spider()