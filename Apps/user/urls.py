from django.conf.urls import url
from Apps.user.views import *  

urlpatterns = [
    url(r'^$', index_user, name='index_user'),
    url(r'^index', index_user, name='index_user'),
    url(r'^new/', create_user, name='create_user'),
    url(r'^edit/(?P<id_user>\d+)/$', update_user, name='edit_user'),
    url(r'^delete/(?P<id_user>\d+)/$', delete_user, name='delete_user'),
    url(r'^view/(?P<id_user>\d+)/$', view_user, name='view_user'),
    url(r'^listar', listUser.as_view(), name='list_user'),
    url(r'^create', createUser.as_view(), name='crear_user'),
    url(r'^update/(?P<pk>\d+)/$', updateUser.as_view(), name='update_user'),
    url(r'^borrar/(?P<pk>\d+)/$', borrarUser.as_view(), name='borrar_user'),
    url(r'^reset/$', password_updated , name='reset_your_password'),
]