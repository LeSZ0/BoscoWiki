"""BoscoWiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from BoscoWiki.views import login_page, logout_page, index, files_page
from django.contrib.auth.views import password_change, password_change_done, default_token_generator, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# 3bc0763c17851984e51c64b746fe42a3/d033e22ae348aeb5660fc2140aec35850c4da997 == Admin

urlpatterns = [
    url(r'^3bc0763c17851984e51c64b746fe42a3/d033e22ae348aeb5660fc2140aec35850c4da997/', admin.site.urls, name='admin'),
    url(r'^post/', include('Apps.post.urls', namespace='post')),
    url(r'^usuario/', include('Apps.user.urls', namespace='usuario')),
    url(r'^rol/', include('Apps.rol.urls', namespace='rol')),
    url(r'^comment/', include('Apps.comment.urls', namespace='comment')),
    url(r'^$', index, name='index'),
    url(r'^login/', login_page, name='login'),
    url(r'^logout/', logout_page, name='logout'),
    url(r'^index/', index, name='index'),
    url(r'^f1l3z/', files_page, name='files'),
    url(r'^reset/pwd/change/$', password_change, 
        {'template_name': 'reset/password_change_form.html'}, name='password_change'),
    url(r'^reset/pwd/done/$', password_change_done, name='password_change_done'),
    url(r'^reset/$', password_reset, 
        {'template_name': 'reset/registration/password_reset_form.html'}, name='password_reset'),
    url(r'^reset/done/$', password_reset_done, 
        {'template_name': 'reset/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)-(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'reset/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/complete/$', password_reset_complete, 
        {'template_name': 'reset/registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
