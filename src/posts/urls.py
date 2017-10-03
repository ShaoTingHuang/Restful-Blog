from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list, 
	post_create, 
	post_detail, 
	post_update, 
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),  # r'^(?P<id>\d+)/$'
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'), # r'^(?P<id>\d+)/edit/$'
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete), # r'^(?P<id>\d+)/delete/$'
]
 