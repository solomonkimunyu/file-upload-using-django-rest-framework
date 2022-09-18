# from django.conf.urls import url
from .views import FileView
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^upload/$', FileView.as_view(), name='file-upload'),
]