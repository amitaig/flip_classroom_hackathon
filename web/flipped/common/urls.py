from django.conf.urls import patterns, url

from common import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^home/$', views.home) 
)
