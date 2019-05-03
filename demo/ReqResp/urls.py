
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^reverse/$', views.ReverseView.as_view(), name='reverse'),

]
