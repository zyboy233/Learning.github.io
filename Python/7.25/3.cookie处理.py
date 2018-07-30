# CookieJar有一些子类,分别是FileCookieJar,LWPCookieJar,MoziliaCookieJar
# CookieJar管理http生成的cookie,负责cookie的存储工作, 向http当中
# 添加指定的cookie
from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# ----------------------------获取cookie
# 生成一个管理cookie的对象
cookie_obj = CookieJar()
# 创建一个支持cookie的对象,对象属于HHTTPCookieProcessor
cookie_handler = HTTPCookieProcessor(cookie_obj) #quote(url,safe=string.printable)
# build_opene内部的实现就是urlopen
# urlopen 只能进行简单的请求,不支持在线验证,cookie,代理等复杂操作
opener = build_opener(cookie_handler)

response = opener.open('http://www.neihanshequ.com')
print(response)

for cookie in cookie_obj:
    print('key:',cookie.name)
    print('value:',cookie.value)
cookie_obj
# ----------------------------------保存cookie
filename = 'neihan.txt'
# 设置cookie保存的文件
cookie_obj = LWPCookieJar(filename=filename)
cookie_handler = HTTPCookieProcessor(cookie_obj)
opener = build_opener(cookie_handler)
response = opener.open('http://neihanshequ.com')
# 保存cookie到指定的文件当中去
# ignore 忽略
# ignore_expires=True 即便目标cookie已经在文件中存在 仍然对齐写入
# ignore_discard 即便目标cookie将要/已经过期,仍然写入
cookie_obj.save(ignore_expires=True,ignore_discard=True)


# 使用本地cookie进行请求
cookie = LWPCookieJar()
cookie.load('neihan.txt')
request = Request('http://neihanshequ.com')
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
response = opener.open(request)
print(response.read().decode())

# 模拟登陆美食杰-----------------------------
cookie = LWPCookieJar(filename='meishi.txt')
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce'
# urlencode对url当中的内容进行编码
# quote 对url当中的中文进行编码
# urlencode()编码的对象为字典类型
# quote 编码的对象为字符串
post_data = urlencode({
    'username':'451253127@qq.com',
    'password':'Msj_zy520520'
})
# 请求url并传参 设置编码方式
request = Request(post_url,bytes(post_data,encoding='utf-8'),headers=headers)
response = opener.open(request)
print(response.read().decode())
cookie.save(ignore_discard=True,ignore_expires=True)
# 利用登陆获取的cookie来请求美食杰首页
cookie = LWPCookieJar()
cookie.load('meishi.txt',ignore_expires=True,ignore_discard=True)
opener = build_opener(HTTPCookieProcessor(cookie))
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
request = Request('https://www.meishij.net/',headers=headers)
# request = Request('https://i.meishi.cc/')
response = opener.open(request)
print(response.read().decode())