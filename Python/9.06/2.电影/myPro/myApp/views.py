from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def myMovie(request):
    # 获取城市信息
    #
    if request.method == 'GET':
        response = requests.get('https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z')

        response_dic = response.json()
        city = response_dic['content']['address_detail']['city']
    else:
        # 如果发现请求方式是post方式  就可以认为是form表单发送的请求
        # 那么直接获取form表单里面name值为city的input标签里面的内容
        city = request.POST['city']
    # 拼接url 获取全部电影信息
    movieUrl = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
    movieData = requests.get(movieUrl).json()
    # 判断电影信息是否请求成功
    if movieData['error'] == 0:
        all_movies = movieData['result']['movie']
        context = {
            'city':city,
            'allMovies':all_movies
        }
    else:
        context = {
            'city':city,
            'error':'无法获取当前城市的电影信息'
        }
    return render(request,'index.html',context)
