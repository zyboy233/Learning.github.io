from django.shortcuts import render
from .models import Three,Four
# Create your views here.
def index(request):
    t1 = Three.objects.create(user='张三1',age='18')
    t2 = Three.objects.create(user='张三2',age='18')

    f1 = Four.objects.create(u_id_id=t1.id,des='11111',font='张三1的爱好')
    f2 = Four.objects.create(u_id_id=t1.id,des='2222',font='张三1的爱好')
    return render(request,'index.html')
def select(request):
    pass
