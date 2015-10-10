from django.conf.urls import patterns, url
from index import views
urlpatterns = patterns('',
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^index', views.index, name='index'),
    url(r'^group/(?P<name>\w{1,50})', views.show_group, name='show_group'),
    url(r'^new_group', views.new_group, name='new_group'),


    url(r'^', views.home, name='home'),
)
