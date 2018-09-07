from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
# Create your views here.

def myWeather(request):
    # if request.method == 'GET':
    #     result = requests.get('http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?').json()
    #     print(result)
    #     weather_datas = result['results'][0]['weather_data']
    # else:
    #     result = requests.get('http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(request.POST['city'])).json()
    #     weather_datas = result['results'][0]['weather_data']
    result = {"error":0,"status":"success","date":"2018-09-06","results":[{"currentCity":"郑州","pm25":"72","index":[{"des":"天气炎热，建议着短衫、短裙、短裤、薄型T恤衫等清凉夏季服装。","tipt":"穿衣指数","title":"穿衣","zs":"炎热"},{"des":"较不宜洗车，未来一天无雨，风力较大，如果执意擦洗汽车，要做好蒙上污垢的心理准备。","tipt":"洗车指数","title":"洗车","zs":"较不宜"},{"des":"各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。","tipt":"感冒指数","title":"感冒","zs":"少发"},{"des":"天气较好，但风力较强，在户外要选择合适的运动，另外考虑到天气炎热，建议停止高强度运动。","tipt":"运动指数","title":"运动","zs":"较不宜"},{"des":"属中等强度紫外线辐射天气，外出时建议涂擦SPF高于15、PA+的防晒护肤品，戴帽子、太阳镜。","tipt":"紫外线强度指数","title":"紫外线强度","zs":"中等"}],"weather_data":[{"date":"周四 09月06日 (实时：32℃)","dayPictureUrl":"http://api.map.baidu.com/images/weather/day/duoyun.png","nightPictureUrl":"http://api.map.baidu.com/images/weather/night/duoyun.png","weather":"多云","wind":"西北风4-5级","temperature":"35 ~ 19℃"},{"date":"周五","dayPictureUrl":"http://api.map.baidu.com/images/weather/day/qing.png","nightPictureUrl":"http://api.map.baidu.com/images/weather/night/qing.png","weather":"晴","wind":"北风3-4级","temperature":"29 ~ 17℃"},{"date":"周六","dayPictureUrl":"http://api.map.baidu.com/images/weather/day/qing.png","nightPictureUrl":"http://api.map.baidu.com/images/weather/night/qing.png","weather":"晴","wind":"南风微风","temperature":"30 ~ 17℃"},{"date":"周日","dayPictureUrl":"http://api.map.baidu.com/images/weather/day/duoyun.png","nightPictureUrl":"http://api.map.baidu.com/images/weather/night/yin.png","weather":"多云转阴","wind":"东南风微风","temperature":"29 ~ 19℃"}]}]}
    weather_datas = result['results'][0]['weather_data']
    context = {
        'city':result['results'][0]['currentCity'],
        'current':weather_datas[0],
        'weather_datas':weather_datas[1:]
    }
    return render(request,'index.html',context)
