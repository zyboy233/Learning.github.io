from django.urls import path
from . import views

urlpatterns = [
    path(r'regist/',views.regist),
    path(r'login/',views.login)
]