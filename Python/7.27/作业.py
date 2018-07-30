# 总结:xpath和bs4和正则的区别
# 总结:数据请求方式的区别
# 举例说明

# xpath
from lxml import etree
# bs4
from bs4 import BeautifulSoup
# 正则
import re
# 数据请求
from urllib.request import urlopen,Request
import requests

# -------------------------------------------------xpath和bs4和正则的区别
                # 总结:
                # xpath与bs4z查找标签的方式不同 见33,42
                # xpath和bs4都具有get方法用于取属性的值 其中xpath也可用 @+属性名 来取属性值
                # xpath使用text()取文本  BeautifulSoup使用get_text()取文本
                # 正则直接正面刚
# 以网站美食杰为例 'http://meishij.net'说明
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

request = Request('http://meishij.net',headers=headers)
response = urlopen(request)
code = response.read().decode()
# print(code)

# xpath
    # etree将响应的字符串code转化为html的标签类型,
    # 通过xpath访问标签的方式匹配查找指定的内容
    # root = etree.HTML(code)
root = etree.HTML(code)
print(type(root))
title = root.xpath('//div[@class="nav"]/ul/li')[0]
# strong_text = title.xpath('.//a/strong/text()') #获取标签文本内容 返回字符串
# strong_text = title.xpath('@class')#获取标签内属性内容 返回列表
strong_text = title.get('class') # get 获取标签内属性内容
print(strong_text)


# bs4
soup = BeautifulSoup(code,'lxml')
print(type(soup))
# id唯一 使用 # + id内容来访问  class不唯一 使用. + class内容来访问
# 返回列表 需要[0]来使用
index = soup.select('.nav ul li a')[0]
print(index)
attr = index.get('class') #取属性的值
print(attr)
text = index.get_text() #取文本
print(text)

# 正则
pattern = re.compile(r'<div class="nav">.*?<li class="current">.*?<strong>(.*?)</strong>',re.S)
result = pattern.findall(code)
print(result)

# -----------------------------------------数据请求方式的区别
# 1.requests
# 请求数据方式不同
response = requests.get('http://meishij.net',headers=headers)
print(response.content) # bytes
print(response.text) # str 解码后

# 2.urlopen Request
request = Request('http://meishij.net',headers=headers)
response = urlopen(request).read() #bytes
response = response.decode() #str 解码后
print(response)

