from django.conf.urls import url
from Apps.post.views import *

urlpatterns = [
    url(r'^$', index_post, name='index_post'),
    url(r'^index/', index_post, name='index_post'),
    url(r'^new/', create_post, name='create_post'),
    url(r'^update/(?P<id_post>\d+)/$', update_post, name='update_post'),
    url(r'^delete/(?P<id_post>\d+)/$', delete_post, name='delete_post'),
    url(r'^category/(?P<id_category>\d+)/$', get_post_category , name='category_post'),
    url(r'^view/(?P<id_post>\d+)/$', view_post , name='view_post'),
    url(r'^search/$', search_post , name='search_post'),
]
