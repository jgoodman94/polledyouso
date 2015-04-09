from django.conf.urls import patterns, url
from polls import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^register/$', views.register),
	#  http://127.0.0.1:8000/polls/login/fb
	url(r'^login/(\w*)', views.login, name='login'),
	# register and login
	url(r'^registerI/$', views.registerI, name='registerI'),
	url(r'^index/$', views.index, name='index'),
)