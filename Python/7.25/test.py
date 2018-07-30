from http.cookiejar import LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
import lxml



cookie_obj = LWPCookieJar(filename='cookie.txt')
cookie_handler = HTTPCookieProcessor(cookie_obj)
opener = build_opener(cookie_handler)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
# url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce'
# data = urlencode({
#     'username':'451253127@qq.com',
#     'password':'Msj_zy520520'
# })
# request = Request(url,headers=headers)
# response = opener.open(request,bytes(data,encoding='utf-8'))
#
# cookie_obj.save(ignore_expires=True,ignore_discard=True)


# 加载本地cookie登陆

cookie_obj = LWPCookieJar()
cookie_obj.load('cookie.txt')
cookie_handler = HTTPCookieProcessor(cookie_obj)
opener = build_opener(cookie_handler)

url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'
request = Request(url,headers=headers)
response = opener.open(request)
code = response.read().decode()
print(code)