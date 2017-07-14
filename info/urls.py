from django.conf.urls import url
from django.contrib import admin
from info import views

urlpatterns = [
    url(r'^create/$', views.user_create, name='user_create'),
    url(r'^(?P<id>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^$', views.user_list, name='user_list'),
    url(r'^(?P<id>\d+)/edit/$', views.user_edit, name='user_edit'),
    url(r'^(?P<id>\d+)/delete/$', views.user_delete, name='user_delete'),
]
