from django.urls import path
from .views import RegisterView,LoginView,LoginOutView,test_json

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    # 注销
    path('logout/',LoginOutView.as_view(),name='logout'),
    # 测试使用
    path('test_json/',test_json)
]