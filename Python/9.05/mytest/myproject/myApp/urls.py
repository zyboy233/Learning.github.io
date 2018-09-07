from django.conf.urls import url
from .views import second_page

urlpatterns = [
    url(r'second/', second_page)
]