from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.
def home(request):
    url = 'https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z'
    data_json = requests.get(url).json()
    print(data_json)
    return render(request,'index.html',{'json':data_json})
def weather(request):
    if request.is_ajax():
        city = request.GET.get('city')
        url = url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback='.format(city)
        data_json = requests.get(url).json()
        return JsonResponse({'json':data_json})
    city = '郑州'
    url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback='.format(city)
    data_json = requests.get(url).json()
    return render(request,'weather.html',{'json':data_json})
def movie(request):
    if request.method == 'GET':
        city = '郑州'
    elif request.method == 'POST':
        city = request.POST.get('city')
    url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
    data_json = requests.get(url).json()
    print(data_json)
    return render(request,'movie.html',{'json':data_json})
def j(request):
    if request.is_ajax():
        city = request.GET.get('city')
        url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
        data_json = requests.get(url).json()
        return JsonResponse({'json': data_json})
    city = '郑州'
    url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
    data_json = requests.get(url).json()
    print('++++++++++')
    return render(request, 'j.html', {'json': data_json})
