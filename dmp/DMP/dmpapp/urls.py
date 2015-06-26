from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
    url(r'^project/$', views.project_detail, name='project_detail'),
    url(r'^project//$', views.project_detail, name='project_detail'),
    
  
    url(r'^updateprojectpost/$', views.project_detail_post, name='project_detail'), 
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^datasets/$', views.DatasetView.as_view(), name='dataset'),
    url(r'^updateds/(?P<pk>[0-9]+)$', views.update_ds,name='updateds'), 
    url(r'^updatedspost/$', views.update_dspost,name='updateds'), 
    
]