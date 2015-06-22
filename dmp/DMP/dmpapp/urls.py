from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^datasets/$', views.DatasetView.as_view(), name='dataset'),
    url(r'^ds/(?P<pk>[0-9]+)/$', views.DatasetDetailView.as_view(), name='datasetdetail'),
    url(r'^updateds/$', views.DatasetDetailView.postDS, name='datasetdetail'),
    url(r'^get_name/$', views.get_name, name='get_name'),
    
    

]