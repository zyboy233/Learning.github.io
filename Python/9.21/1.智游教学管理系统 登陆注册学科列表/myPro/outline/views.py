import datetime

from django.shortcuts import render,redirect
from django.views import View
from stage.models import StageModel
from .models import OutlineModel
from managerApp.models import UserModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class OutlineView(View):
    @method_decorator(login_required)
    def get(self,request,stage_id):
        outlines = OutlineModel.objects.filter(stage_id=stage_id,creator=request.user.id).order_by('number')
        return render(request,'outline/outlines.html',{'outlines':outlines,'stage_id':stage_id})
class AddView(View):
    @method_decorator(login_required)
    def get(self,request,stage_id):
        stages = StageModel.objects.filter(id=stage_id)
        return render(request,'outline/add.html',{"stages":stages})
    def post(self,request):
        stage_id = request.POST['stage_id']
        title = request.POST['title']
        days = request.POST['days']
        advancing = request.POST['advancing']
        remark = request.POST['remark']
        number = request.POST['number']
        user = request.user

        outline = OutlineModel()
        outline.stage_id=stage_id
        outline.title = title
        outline.days=days
        outline.advancing=advancing
        outline.remark=remark
        outline.number = number
        outline.creator = user.id
        outline.save()
        return redirect('/outline/{}'.format(stage_id))
class DetailView(View):
    @method_decorator(login_required)
    def get(self,request,outline_id):
        outline = OutlineModel.objects.get(id=outline_id)
        outline.creator = UserModel.objects.get(id=outline.creator).username
        if outline.updater is not None:
            outline.updater = UserModel.objects.get(id=outline.updater).username
        return render(request,'outline/detail.html',{'outline':outline})
class EditView(View):
    @method_decorator(login_required)
    def get(self,request,outline_id):
        outline = OutlineModel.objects.get(id=outline_id)
        outline.creator = UserModel.objects.get(id=outline.creator).username
        return render(request,'outline/edit.html',{'outline':outline})
    def post(self,request):
        outline_id = request.POST['outline_id']
        outline = OutlineModel.objects.get(id=outline_id)
        if outline:
            outline.title=request.POST['title']
            outline.days=request.POST['days']
            outline.advancing=request.POST['advancing']
            outline.remark=request.POST['remark']
            outline.updater = request.user.id
            outline.update_time = datetime.datetime.now()
            outline.version += 1
            outline.save()
        return redirect('/outline/{}'.format(outline.stage_id))
class DeleteView(View):
    @method_decorator(login_required)
    def get(self,request,outline_id):
        outline = OutlineModel.objects.get(id=outline_id)
        stage_id=outline.stage_id
        if outline:
            outline.delete()
        return redirect('/outline/{}'.format(stage_id))