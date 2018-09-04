from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'red/',views.myFirst),
    url(r'black/',views.mySecond)
]
