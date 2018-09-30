from django.urls import path
from .views import ProgramView,AddView,DetailView,EditView,DeleteView
app_name='program'

urlpatterns=[
    path(r'<outline_id>',ProgramView.as_view(),name='program'),
    path(r'add/<int:outline_id>',AddView.as_view()),
    path(r'add/',AddView.as_view(),name='add'),
    path(r'detail/<int:program_id>',DetailView.as_view(),name='detail'),
    path(r'edit/<int:program_id>',EditView.as_view()),
    path(r'edit/',EditView.as_view(),name='edit'),
    path(r'delete/<int:program_id>',DeleteView.as_view(),name='delete')
]