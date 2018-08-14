from urllib.request import urlopen,Request
import re,os



headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            "Referer":"http://qq9874.pw/cg/index.htm",
            "Cookie":"PHPSESSID=tvrn9t31mavrr30puqr5op06h0; _ga=GA1.2.915138309.1532344348; _gid=GA1.2.1336273637.1532344348; _gat_gtag_UA_15040805_39=1"
        }

class DataManager(object):
    pass

class Spider(object):
    def __init__(self):
        self.name = ''
    def get_code_from_url(self,url):
        request = Request(url,headers=headers)
        response = urlopen(request)
        code = response.read().decode()
        # print(code)
        return code
    def get_sub_url_from_code(self,code):
        pattern = re.compile(r'<a class="c5".*?href="(.*?)".*?>(.*?)</a>',re.S)
        sub_url = pattern.findall(code)
        # print(result)
        return sub_url
    def get_jpg_url_from_sub_code(self,sub_code):
        print(sub_code)
        pattern = re.compile(r'Large_cgurl\[.*?] = "(.*?)";',re.S)
        jpg_url = pattern.findall(sub_code)
        return jpg_url[0:-1]
    def get_jpg_from_jpg_url(self,jpg_url,name):
        try:
            os.makedirs('D:/福利/{}'.format(name))
        except Exception as e:
            print('创建文件夹失败')
        else:
            for index,jpg in enumerate(jpg_url):
                response = urlopen(jpg)
                jpgStr = response.read()
                with open('D:/福利/{}/{}.jpg'.format(name,index),'wb') as j:
                    j.write(jpgStr)
                    j.close()



spider = Spider()
# code = spider.get_code_from_url('http://qq9874.pw/cg_category/101.html')
# # sub_url为列表  内为元组 其内为url和name
# sub_url = spider.get_sub_url_from_code(code)
# sub_code = spider.get_code_from_url(sub_url[0][0])
# jpg_url = spider.get_jpg_url_from_sub_code(sub_code)
# spider.get_jpg_from_jpg_url(jpg_url,'12')

for page in range(1000,1009):
    print(page)
    code = spider.get_code_from_url('http://qq9874.pw/cg_category/{}.html'.format(str(page)))
    # print(code)
    sub_url = spider.get_sub_url_from_code(code)
    print(sub_url)
    for subUrl,name in sub_url:
        print(subUrl,name)
        sub_code = spider.get_code_from_url(subUrl)
        jpg_url = spider.get_jpg_url_from_sub_code(sub_code)
        spider.get_jpg_from_jpg_url(jpg_url,name)

