from django.urls import path
from django.conf.urls import url
from . import views
from .views import RegisterView,LoginView,ActiveView,HomeView,ForgetView,ResetView,ResetPage,SubjectView,EditView,AddView,DeleteView,LogoutView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    # ?P 抓取 并赋值给code
    url(r'^active/(?P<code>\w+)',ActiveView.as_view(),name='active'),
    path(r'home/',HomeView.as_view(),name='home'),
    path(r'forget/',ForgetView.as_view(),name='forget'),
    url(r'^reset/(?P<reset>\w+)',ResetView.as_view(),name='reset'),
    url(r'resetpage/',ResetPage.as_view(),name='resetpage'),
    url(r'^info/',SubjectView.as_view(),name='info'),
    url(r'^edit/',EditView.as_view(),name='edit'),
    url(r'add/',AddView.as_view(),name='add'),
    url(r'delete/',DeleteView.as_view(),name='delete'),
    path(r'',SubjectView.as_view(),name='subject')
]