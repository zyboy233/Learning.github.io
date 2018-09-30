from django.urls import path
from .views import RegistView

urlpatterns = [
    path('regist/',RegistView.as_view(),name='regist')
]