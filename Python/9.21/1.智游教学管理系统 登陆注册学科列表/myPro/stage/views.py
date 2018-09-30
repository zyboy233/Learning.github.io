import datetime
from django.shortcuts import render,render_to_response,redirect
from django.views import View
from stage.models import StageModel
from subject.models import SubjectModel
from managerApp.models import UserModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class StageView(View):
    '''所有阶段'''
    @method_decorator(login_required)
    def get(self,request):
        subject_id = request.GET['subject_id']
        subject_name = SubjectModel.objects.get(id=subject_id).name
        stage_list = StageModel.objects.filter(subject_id=subject_id,creator=request.user.id).order_by('number')
        return render(request,'stage/stage_list.html',{'stage_list':stage_list,'subject_name':subject_name})
class DetailView(View):
    '''阶段详情'''
    @method_decorator(login_required)
    def get(self,request):
        stage_id = request.GET['stage_id']
        # subject_id = request.GET['subject_id']
        stage = StageModel.objects.get(id=stage_id)
        subject = SubjectModel.objects.get(id=stage.subject_id)
        stage.creator = UserModel.objects.get(id=request.user.id).username
        if UserModel.objects.filter(id=stage.updater):
            stage.updater = UserModel.objects.get(id=stage.updater).username

        return render(request,'stage/detail.html',{'stage':stage,
                                            'subject':subject})
class DeleteView(View):
    """删除阶段"""

    @method_decorator(login_required)
    def get(self,request):
        stage_id = request.GET['stage_id']
        stage = StageModel.objects.get(id=stage_id)
        subject_id = stage.subject_id
        if stage:
            stage.delete()
        return redirect('/stage/list/?subject_id={}'.format(subject_id))
class EditView(View):
    '''修改阶段'''

    @method_decorator(login_required)
    def get(self,request):
        stage_id = request.GET['stage_id']
        stage = StageModel.objects.get(id=stage_id)
        stage.creator = UserModel.objects.get(id=stage.creator)
        return render(request,'stage/edit.html',{'stage':stage})
    def post(self,request):
        stage_id = request.POST['stage_id']
        stage = StageModel.objects.get(id=stage_id)
        if stage:
            stage.title = request.POST['title']
            stage.days = request.POST['days']
            stage.project = request.POST['project']
            stage.number = request.POST['number']
            stage.teaching = request.POST['teaching']
            stage.learning = request.POST['learning']
            stage.sharing = request.POST['sharing']
            stage.remark = request.POST['remark']
            stage.updater = request.user.id
            stage.update_time = datetime.datetime.now()
            stage.version += 1
            stage.save()
        return redirect('/stage/list/?subject_id={}'.format(stage.subject_id))
class AddView(View):
    '''添加阶段'''

    @method_decorator(login_required)
    def get(self,request):
        subjects = SubjectModel.objects.all()
        return render(request,'stage/add.html',{'subjects':subjects})
    def post(self,request):
        subject_id = request.POST['subject_id']
        stage = StageModel()
        stage.subject_id = subject_id
        stage.title = request.POST['title']
        stage.days = request.POST['days']
        stage.number = request.POST['number']
        stage.project = request.POST['project']
        stage.sharing = request.POST['sharing']
        stage.learning = request.POST['learning']
        stage.remark = request.POST['remark']
        stage.teaching = request.POST['teaching']
        stage.creator = request.user.id
        stage.save()
        return redirect('/stage/list/?subject_id={}'.format(subject_id))