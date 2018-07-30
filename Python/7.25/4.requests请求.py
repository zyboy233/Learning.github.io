import requests
import json

from prettyprinter import pprint

class Weather(object):
    def __init__(self):
        # 获取本地信息
        self.location_url = 'http://api.map.baidu.com/location/ip?&ak=KQvhEkxc6mFCAYHTblC3NGVmxzxIWk0E&coor=bd09ll'
        # 获取天气信息
        self.weather_url = 'http://api.map.baidu.com/telematics/v3/weather?output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?&location='
    def start_spider(self):
        cityName = self.get_location()
        self.get_weather_info(cityName)

        while True:
            cityName = input('请输入城市名字:')
            if cityName == 'E':
                return
            self.get_weather_info(cityName)
    def get_weather_info(self,cityName):
        url = self.weather_url + cityName
        response = requests.get(url)
        # print(response.reason)
        weather_dic = json.loads(response.content)
        pprint(weather_dic)
        for dayDic in weather_dic['results'][0]['weather_data']:
            print('{}'.format(dayDic['date']))
            print('温度:{}'.format(dayDic['temperature']))
    def get_location(self):
        response = requests.get(self.location_url)
        # 获取网页的内容
        # print(response.content)
        # 将内容转化成字典对象
        result_dic = json.loads(response.content)
        # pprint(result_dic)
        city = result_dic['content']['address_detail']['city']
        return city
w = Weather()
w.start_spider()
