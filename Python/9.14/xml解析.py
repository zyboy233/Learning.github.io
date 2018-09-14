import requests
import gzip
from xml.dom.minidom import parse
import xml.dom.minidom

url = 'http://flash.weather.com.cn/wmaps/xml/xinyang.xml'

response = requests.get(url)

# 当服务器返回的内容编码格式为gzip时
# print(response.apparent_encoding)
# response = gzip.decompress(response.content).decode("utf-8")

print(response.apparent_encoding)
response = response.content.decode('utf-8')

with open('weather.xml','w',encoding='utf-8') as f:
    f.write(response)
    f.close()

# 转化为DOM对象
DOMTree = xml.dom.minidom.parse('weather.xml')
collection = DOMTree.documentElement

# 获取标签
city_list = collection.getElementsByTagName('city')
print(len(city_list))
for city in city_list:
    # 获取属性值
    print(city.getAttribute('cityname'))
    print(city.getAttribute('temNow'),'摄氏度')