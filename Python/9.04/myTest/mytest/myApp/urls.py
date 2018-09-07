from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'test/',views.home),
    url(r'search_form/',views.form_search),
    url(r'search/',views.search),
    url(r'add',views.add_user),
    url(r'receive',views.receive_user),
    url(r'post',views.receive_user_post)
]