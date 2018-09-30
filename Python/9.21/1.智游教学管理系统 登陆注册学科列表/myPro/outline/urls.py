from django.urls import path
from .views import OutlineView,AddView,DetailView,EditView,DeleteView
app_name='outline'

urlpatterns = [
    path(r'add/<int:stage_id>',AddView.as_view(),name = 'add'),
    path(r'addinfo/',AddView.as_view(),name = 'addinfo'),
    path(r'<int:stage_id>',OutlineView.as_view(),name = 'outlines'),
    path(r'detail/<int:outline_id>',DetailView.as_view(),name='detail'),
    path(r'edit/<int:outline_id>',EditView.as_view()),
    path(r'edit/',EditView.as_view(),name='edit'),
    path(r'delete/<int:outline_id>',DeleteView.as_view(),name='delete')
]