import datetime

from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.views import View
from .models import SubjectModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from managerApp.models import UserModel
# Create your views here.

# render 和 render_to_response
# render把request作为参数直接传递到html页面
# render_to_response 里不能使用全局对象request里的属性

def index(request):
    if request.method == "POST":
        # 处理post请求
        pass
    # subjects = SubjectModel.objects.all()
    subjects = SubjectModel.object.order_by("number")
    return render(request,'subject/home.html',{'subjects':subjects})

class SubjectView(View):
    def get(self,request):
        subjects = SubjectModel.objects.filter(creator=request.user.id).order_by('number')
        return render(request,'subject/home.html',{'subjects':subjects})
    def post(self,request):
        return render(request,'subject/home.html')
class DetailView(View):
    def get(self,request):
        user = request.user
        subject_id = request.GET['subject_id']
        subject = SubjectModel.objects.get(id=subject_id)
        subject.creator = UserModel.objects.get(id=user.id).username
        if UserModel.objects.filter(id=subject.updater):
            subject.updater = UserModel.objects.filter(id=subject.updater)[0].username
        return render(request,'subject/detail.html',{'subject':subject})

class EditView(View):
    @method_decorator(login_required)
    def get(self,request):
        subject_id = request.GET['subject_id']
        subject = SubjectModel.objects.get(id=subject_id)
        subject.creator = UserModel.objects.get(id=subject.creator)
        return render(request,'subject/edit.html',{'subject':subject})

    @method_decorator(login_required)
    def post(self,request):
        user =request.user
        subject_id = request.POST['subject_id']
        name = request.POST['name']
        amount = request.POST['amount']
        number = request.POST['number']
        days = request.POST['days']
        assurance = request.POST['assurance']
        remark = request.POST['remark']

        subject = SubjectModel.objects.get(id=subject_id)
        if subject:
            subject.name = name
            subject.days = days
            subject.amount = amount
            subject.number = number
            subject.assurance = assurance
            subject.remark = remark
            subject.updater = user.id
            subject.update_time = datetime.datetime.now()
            subject.version += 1
            subject.save()
        return redirect('/subject')
class AddView(View):
    @method_decorator(login_required)
    def get(self,request):
        return render(request,'subject/add.html')

    @method_decorator(login_required)
    def post(self,request):
        print(request)
        name = request.POST['name']
        amount = request.POST['amount']
        number = request.POST['number']
        days = request.POST['days']
        assurance = request.POST['assurance']
        remark = request.POST['remark']
        # 把request里的user赋值给自定义的user
        user = request.user
        subject = SubjectModel()
        subject.name = name
        subject.days = days
        subject.amount = amount
        subject.number = number
        subject.assurance = assurance
        subject.remark = remark
        subject.updater = 0
        subject.creator = user.id
        subject.save()

        return redirect('/subject')

class DeleteView(View):
    @method_decorator(login_required)
    def get(self,request):
        subject_id = request.GET['subject_id']
        subject = SubjectModel.objects.get(id=subject_id)
        user = request.user
        if subject and user.id == subject.creator:
            subject.delete()
        return redirect('/subject')