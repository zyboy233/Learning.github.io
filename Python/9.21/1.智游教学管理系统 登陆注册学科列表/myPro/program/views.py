from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
from .models import ProgramModel
from outline.models import OutlineModel
from stage.models import StageModel
from django.core import serializers
from managerApp.models import UserModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
import datetime
# Create your views here.

class ProgramView(View):
    @method_decorator(login_required)
    def get(self,request,outline_id):
        programs = ProgramModel.objects.filter(outline_id=outline_id,creator=request.user.id).order_by('number')
        return render(request,'program/programs.html',{'programs':programs,'outline_id':outline_id})

class AddView(View):
    @method_decorator(login_required)
    def get(self,request,outline_id):

        return render(request,'program/add.html',{'outline_id':outline_id})
    def post(self,request):
        program = ProgramModel()
        outline = OutlineModel.objects.get(id=request.POST['outline_id'])
        program.stage_id=outline.stage_id
        program.outline_id = request.POST['outline_id']
        program.number = request.POST['number']
        program.sign=request.POST['sign']
        program.digest= request.POST['digest']
        program.prepare=request.POST['prepare']
        program.process=request.POST['process']
        program.attention=request.POST['attention']
        program.exercise=request.POST['exercise']
        program.share=request.POST['share']
        program.management=request.POST['management']
        program.remark=request.POST['remark']
        program.creator = request.user.id
        program.save()
        return redirect('/program/{}'.format(request.POST['outline_id']))

class DetailView(View):
    @method_decorator(login_required)
    def get(self,request,program_id):
        program=ProgramModel.objects.get(id=program_id)
        stage = StageModel.objects.get(id=program.outline_id)
        outline = OutlineModel.objects.get(id=program.outline_id)
        program.creator = UserModel.objects.get(id=program.creator).username
        if program.updater:
            program.updater = UserModel.objects.get(id=program.updater)
        return render(request,'program/detail.html',{'program':program,'stage':stage,'outline':outline})

class EditView(View):
    @method_decorator(login_required)
    def get(self,request,program_id):
        program = ProgramModel.objects.get(id=program_id)
        subject_id = StageModel.objects.get(id=program.stage_id).subject_id
        stages = StageModel.objects.filter(subject_id=subject_id)
        outlines = OutlineModel.objects.filter(stage_id=program.stage_id)
        program.creator = UserModel.objects.get(id=program.creator)
        return render(request,'program/edit.html',{'program':program,'stages':stages,'outlines':outlines})
    def post(self,request):
        try:
            stage_id = request.POST['stage_id']
            outlines = OutlineModel.objects.filter(stage_id=stage_id)
            outlines = serializers.serialize("json", outlines)
            outlines = json.loads(outlines)
            # print(outlines)
            # print(type(outlines))
            return JsonResponse({'outlines': outlines})
        except Exception as e:
            program = ProgramModel.objects.get(id=request.POST['program_id'])
            program.number = request.POST['number']
            program.sign=request.POST['sign']
            program.digest=request.POST['digest']
            program.prepare=request.POST['prepare']
            program.process=request.POST['process']
            program.attention=request.POST['attention']
            program.exercise=request.POST['exercise']
            program.share=request.POST['share']
            program.management=request.POST['management']
            program.remark=request.POST['remark']
            program.updater = request.user.id
            program.update_time = datetime.datetime.now()
            program.version += 1
            program.save()
            return redirect('/program/{}'.format(program.outline_id))

class DeleteView(View):
    @method_decorator(login_required)
    def get(self,request,program_id):
        program = ProgramModel.objects.get(id=program_id)
        outline_id = program.outline_id
        if program:
            program.delete()
        return redirect('/program/{}'.format(outline_id))