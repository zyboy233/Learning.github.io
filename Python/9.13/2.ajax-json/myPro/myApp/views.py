from django.shortcuts import render
from django.http import JsonResponse
# View类为自定义视图类 该类可以响应get post方法
from django.views.generic import View
from django.core.paginator import Paginator
import requests
# Create your views here.
def index(request):
    url = 'https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z'
    data_json = requests.get(url).json()

    return render(request,'index.html',{'json':data_json})

def weather(request):
    if request.is_ajax():
        city = request.GET.get('city')
        print(city)
        url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback='.format(city)
        data_json = requests.get(url).json()
        return JsonResponse({'json': data_json})
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback='
    data_json = requests.get(url).json()
    return render(request,'weather.html',{'json':data_json})

def movie(request):
    if request.is_ajax():
        city = request.POST.get('city')
        url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=fCWHp1a9QdsHwfPbHZ20LGLzgpKHEGrc&output=json'.format(city)
        data_json = requests.get(url).json()
        return JsonResponse({'json':data_json})
    city = '郑州'
    url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=fCWHp1a9QdsHwfPbHZ20LGLzgpKHEGrc&output=json'.format(city)
    data_json = requests.get(url).json()
    return render(request,'movie.html',{'json':data_json})

class MovieView(View):
    # 该方法可以响应所有的get请求
    def get(self,request):
        print(request.GET.get('page'))
        if request.GET.get('city'):
            city = request.GET.get('city')
            print('+++++++++++++++++++')
            print(city)
        else:
            city = '郑州'
        url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=fCWHp1a9QdsHwfPbHZ20LGLzgpKHEGrc&output=json'.format(city)
        data_json = requests.get(url).json()
        paginator = Paginator(data_json['result']['movie'],8)
        pages_num = paginator.num_pages
        if request.GET.get('page'):
            page = paginator.page(int(request.GET.get('page')))
        else:
            page = paginator.page(1)
        print(page.number)
        return render(request,'movie.html',{'page':page,'pages_num':pages_num,'city':city})
    def post(self,request):
        print(request.POST.get('page'))
        city = request.POST.get('city')
        url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=fCWHp1a9QdsHwfPbHZ20LGLzgpKHEGrc&output=json'.format(city)
        data_json = requests.get(url).json()
        paginator = Paginator(data_json['result']['movie'],8)
        pages_num = paginator.num_pages
        page = paginator.page(1)
        print(page.number)
        return render(request,'movie.html',{'page':page,'pages_num':pages_num,'city':city})
class WeatherView(View):
    def get(self,request):
        city = request.GET.get('city')
        if city:
            url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
        else:
            url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(
                '郑州')
        data_json = requests.get(url).json()
        print('-------------------------------------')
        if city:
            return JsonResponse({'json':data_json})
        return render(request,'weather.html',{'json':data_json})
class JoyView(View):
    def get(self,request):
        page = request.GET.get('page')
        if page:
            url = 'https://www.apiopen.top/satinGodApi?type=2&page={}'.format(page)
            page = int(page)
        else:
            page = 1
            url = 'https://www.apiopen.top/satinGodApi?type=2&page=1'
        data_json = requests.get(url).json()
        rg = list(range(1,11))
        # if page!=1:
        #     return JsonResponse({'json':data_json})
        return render(request,'joy.html',{'json':data_json,'range':rg,'page':page})
class GirlView(View):
    def get(self,request):
        page = request.GET.get('page')
        if page:
            url = 'https://www.apiopen.top/meituApi?page={}'.format(page)
            data_json = requests.get(url).json()
            return JsonResponse({'json':data_json['data'],'numList':list(range(1,len(data_json['data'])))})
        url = 'https://www.apiopen.top/meituApi?page=1'
        data_json = requests.get(url).json()
        return render(request,'girl.html',{'json':data_json['data'],'numList':list(range(1,len(data_json['data'])))})