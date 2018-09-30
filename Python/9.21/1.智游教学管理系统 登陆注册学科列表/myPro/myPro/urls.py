"""myPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from managerApp.views import LoginView
# from subject.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    # 首页
    path('',LoginView.as_view(),name='index'),
    path('user/',include('managerApp.urls')),
    path('subject/',include('subject.urls',namespace='subject')),
    path('stage/',include('stage.urls',namespace='stage')),
    path('outline/',include('outline.urls',namespace='outline')),
    path('program/',include('program.urls',namespace='program'))
]
