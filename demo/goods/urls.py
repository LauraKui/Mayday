
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^list/$', views.ListModelMixin, name='list'),
    # url(r'^create/$', views.CreateModelMixin, name='create'),
    url(r'^book/$', views.BookView.as_view(), name='book'),
    url(r'^goods/$', views.GoodsView.as_view(), name='goods'),
    url(r'^data/$', views.GetData.as_view(), name='data'),
    url(r'^change/$', views.ChangeData.as_view(), name='change'),


]
