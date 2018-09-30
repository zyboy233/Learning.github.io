from django.shortcuts import render
from django.views import View
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

class RegistView(View):
    def get(self,request):
        return render(request,'regist.html')
    get = staff_member_required(get)