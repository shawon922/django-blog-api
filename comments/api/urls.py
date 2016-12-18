from django.conf.urls import url
from .views import (
    CommentListAPIView,
    CommentDetailAPIView
)

app_name = 'comments'

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^delete/(?P<id>\d+)/$', views.delete_comment, name='delete'),
]

