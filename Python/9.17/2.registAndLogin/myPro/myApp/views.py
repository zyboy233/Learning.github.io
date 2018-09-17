from django.shortcuts import render
from django.views import View
# Create your views here.
def index(request):
    return render(request,'index.html')
def regist(request):
    return render(request,'register.html')

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')