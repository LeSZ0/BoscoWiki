from django.conf.urls import url
from Apps.rol.views import *

urlpatterns = [
    url(r'^$', index_rol, name='index_rol'),
    url(r'^index', index_rol, name='index_rol'),
    url(r'^new/', createRol.as_view(), name='create_rol'),
    url(r'^update/(?P<pk>\d+)/', updateRol.as_view(), name='update_rol'),
    url(r'^delete/(?P<pk>\d+)/', deleteRol.as_view(), name='delete_rol'),
]