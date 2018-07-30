import os
from urllib.request import urlretrieve
import requests
from lxml import etree

if os.path.exists('D:/images'):
    os.rmdir('D:/images')
os.mkdir('D:/images')
os.chdir('D:/images')

current_page = 1
def get_image_with_code(url):
    global current_page
    # 总结:xpath和bs4和正则的区别
    # 总结:数据请求方式的区别
    # 举例说明
    # response = urlopen().read().decode()
    # response = requests.get(url).content
    response = requests.get(url).text
    # print(response)

    code = etree.HTML(response)
    img_list = code.xpath('//div[@class="il_img"]/a/img')
    print(img_list)

    print('正在下载第{}页'.format(current_page))
    # 创建对应页面的文件夹
    if not os.path.exists('D:/images/page{}'.format(current_page)):
        os.mkdir('D:/images/page{}'.format(current_page))
    # 进入子文件夹
    os.chdir('D:/images/page{}'.format(current_page))
    for img in img_list:
        img_src = img.get('src')
        img_alt = img.get('alt')
        # img_src = img.xpath('@src')
        # img_alt = img.xpath('@alt')
        urlretrieve(img_src,img_alt+'.jpg')
    # 局部变量 声明的作用 是告诉程序该变量是个什么类型的变量
    current_page += 1
    # 返回父文件夹
    os.chdir(os.path.pardir)

    # 如果还有下一页则返回[Element a ip]
    # 如果没有下一页 则返回[]
    next_page_url = code.xpath('//a[@class="page-next"]')
    print(next_page_url)
    if len(next_page_url) == 0:
        print('已经到最后一页')
        return
    else:
        href = next_page_url[0].get('href')
        full_url = 'http://www.ivsky.com' + href
        get_image_with_code(full_url)

get_image_with_code('http://www.ivsky.com/tupian/meishishijie/')

# 爬虫流程
# 1.拼接url
# 2.获取User-Agent,设置代理
# 3.请求url, urlopen  requests
# 4.获取响应 (response response.read() response.content  response.text)
#     获取cookie
# 5.获取源码中指定数据(re, xpath , bs4)
# 6.美化数据 正则 strip()
# 7.保存(文件读写,sqlite3, xlwt)