from django.conf.urls import patterns, url
from polls import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^index/$|^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/', views.detail, name='detail'),
    url(r'^submitq/$', views.submitq, name='submitq'),
    url(r'^answered/(?P<question_id>\d+)/(?P<question_answer>.+)/', views.answered, name='answered'),
	url(r'^login/(\w*)', views.login, name='login'),
	# register and login
	url(r'^registerI/$', views.registerI, name='registerI'),
)