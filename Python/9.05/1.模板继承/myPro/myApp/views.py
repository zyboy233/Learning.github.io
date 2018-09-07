from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{'title':'首页'})
def home(request):
    return render(request,'home.html',{'title':'主页'})