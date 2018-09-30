from django.urls import path
from django.conf.urls import url
from .views import LessonView

# url(r'^active/(?P<code>\w+)',ActiveView.as_view(),name='active'),

urlpatterns = [
    # url(r'(?P<id>\w+)',LessonView.as_view(),name='lesson')
    path(r'<int:id>/',LessonView.as_view(),name='lesson')
]