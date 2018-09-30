from django.urls import path
from django.conf.urls import url
from . import views
from .views import RegisterView,LoginView,ActiveView,HomeView,ForgetView,ResetView,ResetPage

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    # ?P 抓取 并赋值给code
    url(r'^active/(?P<code>\w+)',ActiveView.as_view(),name='active'),
    path(r'home/',HomeView.as_view(),name='home'),
    path(r'forget/',ForgetView.as_view(),name='forget'),
    url(r'^reset/(?P<reset>\w+)',ResetView.as_view(),name='reset'),
    url(r'resetpage/',ResetPage.as_view(),name='resetpage')
]