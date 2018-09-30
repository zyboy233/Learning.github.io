from django.urls import path
from django.conf.urls import url
from .views import RegistView,ActiveView,LoginView,ForgetView,ResetView
from .views import page
urlpatterns = [
    path('regist/',RegistView.as_view(),name = 'regist'),
    path('page/',page),
    url(r'^active/(?P<code>\w+)',ActiveView.as_view(),name='active '),
    path(r'login/',LoginView.as_view(),name='login'),
    path('forget/',ForgetView.as_view(),name='forget'),
    url(r'reset/(?P<code>\w+)',ResetView.as_view(),name='reset')
]