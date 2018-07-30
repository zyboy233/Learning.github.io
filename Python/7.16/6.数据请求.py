# http url ip
# url 网址 lib library 图书馆   地址库
# request 请求
from urllib.request import urlopen
# parse 解析 quote 引用
from urllib.parse import quote
import string

# urlopen不支持中英文混写 之所以能在url中看到中文
# 是因为浏览器处于友好目的特意显示
# 但是在url执行的时候  中文会被转码
# 如果不进行转码 程序会报错
url = 'http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback='
reponse = urlopen(quote(url,safe = string.printable))
reponseData = reponse.read().decode('utf-8')
print(reponseData)

# 地址栏不支持使用中文  所以需要进行转码
# 转码的时候 不但会将一些中文进行转码
# 同时也会将一些特殊的符号进行转码 比如: ?
# 如果不想让这些特殊符号进行转码
# 就要使用安全转码(指挥转码中文)
print('没有使用safa \n{}'.format(quote(url)))
print('使用了safe \n{}'.format(quote(url,safe=string.printable)))

import json
from prettyprinter import pprint

reponseJson = json.loads(reponseData)
pprint(reponseJson)

print(reponseJson['date'])
# for dict in reponseJson['result'][0]['index']:


