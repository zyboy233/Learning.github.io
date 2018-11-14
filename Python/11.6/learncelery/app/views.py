from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import task_add

# Create your views here.

def add(request):
    task_add.delay(2, 4)
    return HttpResponse('OK')