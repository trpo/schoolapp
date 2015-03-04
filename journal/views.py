from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from journal.models import Subject
from django.template import RequestContext, loader




def index(request):
    latest_subject_list = Subject.objects.order_by('-id')[:5]
    template = loader.get_template('journal/index.html')
    context = RequestContext(request, {
        'latest_subject_list': latest_subject_list,
    })
    return HttpResponse(template.render(context))


def detail(request, question_id):
    return HttpResponse("You're looking at subject %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of subject %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on subject %s." % question_id)


# class PostsListView(ListView): # представление в виде списка
#     model = Subject    

# def index(request):
#     subject_list = Subject.objects
    
#     return HttpResponse(subject_list)