from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
def ajax_get(request):
    # 判断当前请求方式是否为ajax请求
    if request.is_ajax():
        city = request.GET.get('city')
        print(city)
        return JsonResponse({'content':'这是ajax请求'})
        # return render(request,'home.html',{'content':'这是ajax请求'})
    else:
        return JsonResponse({'content':'这是ajax请求'})
        # return render(request,'index.html',{'content':'这是假的ajax请求'})