from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^project_new/$', views.project_new),
    url(r'^project/(?P<pk>[0-9]+)/$', views.project_get),
    url(r'^projectpost/(?P<pk>[0-9]+)/$', views.project_post),
    url(r'^projectpost//', views.project_post),
     
    url(r'^dataset/(?P<pk>[0-9]+)/$', views.dataset_get),  
    url(r'^dataset_new/$', views.dataset_new),  
    
    url(r'^datasetpost/(?P<pk>[0-9]+)/$', views.dataset_post),  
    url(r'^dataset_del/(?P<pk>[0-9]+)/$', views.dataset_del),  
    
    url(r'^datasetpost//$', views.dataset_post),  
    
    
    
     
    
    #url(r'^updateds/(?P<pk>[0-9]+)/$', views.update_ds,name='updatedsss'),   
    
    #url(r'^updateds/$', views.update_ds,name='updateds'), 
    
    url(r'^datasets/$', views.DatasetView.as_view(), name='dataset'),
   
    url(r'^updateds//$', views.DatasetView.as_view(), name='dataset'),
    #url(r'^project//$', views.project_detail, name='project_detail'),
    
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    
]