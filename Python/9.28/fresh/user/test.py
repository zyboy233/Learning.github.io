
# n = int(input('请输入n:'))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# list = [1,2,3,4,5,6]

# for i in list:

import os
# os.remove('file.txt')

# t = (1,2,3,4)
# l = list(t)
# print(l)

# 请求:
from urllib.request import urlopen,Request,urlretrieve,build_opener,ProxyHandler,build_opener
# import requests 同上
# Request:封装请求
# urlopen():请求响应
# urlretrieve():下载文件
# ProxyHandler():代理
# build_opener():扩展请求
# 解析:
# 正则(re):
# import re
# xpath:
# from lxml import etree
# bs4:
# from bs4 import BeautifulSoup

a = {
        "var1": {"key6", "data2"},
        "var2":{"key2", "data1"},
        "var3": {
            "dataw", "333", "bbss"
        }
     }

str = 'abbccc'

s = {1,2,3}
print(type(s),s)

for key,val in a.items():
    for value in val:
        if value.isdigit():
            print(key,value)
