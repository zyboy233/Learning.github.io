from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_page(request):
    content = {
        'hello':'hello world'
    }
    return render(request,'page1.html',content)
def second_page(request):
    content = {
        'hello': 'hello world'
    }
    return render(request, 'page2.html', content)