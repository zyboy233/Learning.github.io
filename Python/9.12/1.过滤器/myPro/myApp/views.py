from django.shortcuts import render

# Create your views here.
def index(request):
    str = 'ABCDEFGhijklmn'
    return render(request,'index.html',{'content':str})