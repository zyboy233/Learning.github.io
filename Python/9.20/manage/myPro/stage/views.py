from django.shortcuts import render
from django.views import View
from myApp.models import Subject
# Create your views here.

class LessonView(View):
    def get(self,request,id):
        stages = Subject.objects.filter(id=id)
        return  render(request,'stage/lesson.html',{'stages':stages})