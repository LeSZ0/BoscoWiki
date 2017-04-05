from django.conf.urls import url
from Apps.comment.views import *

urlpatterns = [
    url(r'^$', index_comment, name='index_comment'),
    url(r'^index/', index_comment, name='index_comment'),
    url(r'^new/(?P<id_post>\d+)/$', create_comment, name='create_comment'),
    url(r'^delete/(?P<id_comment>\d+)/$', delete_comment, name='delete_comment'),
]