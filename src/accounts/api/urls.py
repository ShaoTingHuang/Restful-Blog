from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	)

urlpatterns = [
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    # url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    # url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),  # r'^(?P<id>\d+)/$'
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'), # r'^(?P<id>\d+)/delete/$'
]
 