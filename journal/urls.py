from django.conf.urls import patterns, url

# from journal.views import PostsListView

from journal import views

urlpatterns = patterns('',
    # url(r'^$',  PostsListView.as_view(), name='list'),

    url(r'^$', views.home_user, name='home_user'),
    # ex: /polls/5/
    # url(r'^(?P<user_id>\d+)$', views.student_subject, name='student_subject'),
    # # ex: /polls/5/results/
    url(r'^(?P<user_id>\d+)/results/$', views.student_subject, name='student_subject')
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)