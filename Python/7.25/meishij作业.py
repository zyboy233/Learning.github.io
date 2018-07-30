

# 美食节 使用cookie模拟登陆 获取网页源码
# 使用xpath得到用户信息 存储到excel表格

from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,build_opener,HTTPCookieProcessor
from urllib.parse import urlencode
from lxml import etree
import xlwt

# 获取cookie
fileName = 'meishij.txt'
# 使用继承自CookieJar类的LWPCookieJar类实例化一个管理cookie的对象
# 并传入file那么参数
cookie_obj = LWPCookieJar(filename=fileName)
# 实例化一个支持cookie的扩展类对象
cookie_handler = HTTPCookieProcessor(cookie_obj)
# 构建一个功能更多的请求url的方式
opener = build_opener(cookie_handler)
response = opener.open('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce')
# 保存cookie
cookie_obj.save(ignore_discard=True,ignore_expires=True)

# 使用本地cookie模拟用户登陆
cookie = LWPCookieJar()
cookie.load('meishij.txt')
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
data = urlencode({
    'username':'451253127@qq.com',
    'password':'Msj_zy520520'
})
request = Request(post_url,headers=headers)
response = opener.open(request,bytes(data,encoding='utf-8'))
code = response.read().decode()
root = etree.HTML(code)
print(root)
name_list = root.xpath('//div[@class="info1"]/h1/text()[1]')
name = name_list[0].replace('\t','')

grade_list = root.xpath('//span[@class="info"]/em[1]/a/text()')
grade = grade_list[0]

other_list = root.xpath('//span[@class="info"]/em/text()')

workBook = xlwt.Workbook()
sheet = workBook.add_sheet('info_meishij')
sheet.write(0,0,name)
sheet.write(0,1,grade)
sheet.write(0,2,other_list[0])
sheet.write(0,3,other_list[1])
sheet.write(0,4,other_list[2])
workBook.save('meishij.xls')
