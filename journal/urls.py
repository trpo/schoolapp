from django.conf.urls import patterns, url

# from journal.views import PostsListView

from journal import views

urlpatterns = patterns('',
    # url(r'^$',  PostsListView.as_view(), name='list'),

    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)