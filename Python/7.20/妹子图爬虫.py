
import re,os,time
from urllib.request import Request,urlopen

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',

    "Host":"www.mmjpg.com",
    "Referer":"http://www.mmjpg.com/home/3"
}

def get_code_from_url(base_url):
        url = '{}'.format(base_url)
        request = Request(url,headers=headers)

        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('获取失败')
            return e
        else:
            return code
def get_sub_url_from_code(code):
    print(code)
    pattern = re.compile(r'<li.*?<span class="title">.*?<a href="(.*?)".*?>',re.S)
    sub_url = pattern.findall(code)
    return sub_url

def get_all_jpg_url_from_sub_code(sub_code,sub_url):
    base_jpg_url = sub_url+'/'
    pattern_pages = re.compile(r'<div class="page".*?<i></i>.*?<a href.*?>(.*?)</a>',re.S)
    pattern_url_jpg=re.compile(r'<div class="content".*?<img src="(.*?)".*?>',re.S)
    pages_jpg = int(pattern_pages.findall(sub_code)[0])
    print(pages_jpg)
    jpg_url_list = []

    for page in range(1,pages_jpg+1):
        page_url = base_jpg_url+str(page)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',

            "Host": "www.mmjpg.com",
            "Referer": "{}".format(base_jpg_url)
        }
        request = Request(page_url,headers=headers)
        response = urlopen(request)
        page_code = response.read().decode()
        # page_code = get_code_from_url(page_url)
        jpg_url = pattern_url_jpg.findall(page_code)[0]
        print(jpg_url)
        jpg_url_list.append(jpg_url)
    # print(jpg_url_list)
    return jpg_url_list
def get_jpg_from_jpg_list(jpg_list=[]):
    num = 1
    nameList = jpg_list[0].split('/')
    dirName = nameList[4]
    try:
        os.makedirs('D:/meizitu/{}'.format(dirName))
    except Exception as e :
        print('文件夹已存在')
    else:
        for jpg_url in jpg_list:
            with open('D:/meizitu/{}/{}.jpg'.format(dirName,num),'wb')as j:
                head = {
                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',

                    # "Host": "www.mmjpg.com",
                    "Referer":"http://www.mmjpg.com/home/4"
                }

                request = Request(jpg_url,headers=head)
                response = urlopen(request)
                responseStr = response.read()
                j.write(responseStr)
                j.close()
            num+=1
for i in range(10,96):
    print(i)
    page = 'http://www.mmjpg.com/home/{}'.format(i)
    code = get_code_from_url(page)
    sub_url_list = get_sub_url_from_code(code)
    for sub_url in sub_url_list:
        sub_code = get_code_from_url(sub_url)
        jpg_url_list = get_all_jpg_url_from_sub_code(sub_code,sub_url)
        get_jpg_from_jpg_list(jpg_url_list)


# page = 'http://www.mmjpg.com/home/3'
# code = get_code_from_url(page)
# url_sub = get_sub_url_from_code(code)
# print(url_sub)
# sub_code = get_code_from_url(url_sub[0])
# # print(sub_code)
# jpg_url_list = get_all_jpg_url_from_sub_code(sub_code,url_sub[0])
# get_jpg_from_jpg_list(jpg_url_list)
