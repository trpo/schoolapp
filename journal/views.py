from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView

from django.http import HttpResponse

from journal.models import Subject

class PostsListView(ListView): # представление в виде списка
    model = Subject    

def index(request):
    subject_list = Subject.objects
    
    return HttpResponse(subject_list)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)