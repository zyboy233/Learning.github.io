from django.urls import path

from .views import StageView,EditView,DetailView,DeleteView,AddView
app_name='stage'

urlpatterns = [
    path('list/',StageView.as_view(),name='stage_list'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('edit/',EditView.as_view(),name='edit'),
    path('delete/',DeleteView.as_view(),name='delete'),
    path('add/',AddView.as_view(),name='add')
]