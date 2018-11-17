from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from images.forms import  ImageCreateForm
from images.models import Image
# Create your views here.

@login_required
def image_create(request):
    if request.method =='POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            # 表单验证通过
            cd =form.cleaned_data
            new_item = form.save(commit=False)
            # 把当前用户附加到数据对象上
            new_item.user = request.user
            new_item.save()
            messages.success(request,'图片添加成功!')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
        print(form)
    return render(request,'images/create.html',{'selection':'images','form':form})

def image_detail(request,id,slug):
    image = get_object_or_404(Image,id=id, slug=slug)
    return render(request,'images/detail.html',{'image':image,'selection':'images'})