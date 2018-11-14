from django.urls import path
from wechat.views import handle_wx,create_menu,add_image
urlpatterns = [
    path('',handle_wx),
    path('create_menu/',create_menu),
    path('add_image/',add_image)
]