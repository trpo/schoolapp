from django.shortcuts import get_object_or_404, render

from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template import RequestContext, loader

from journal.models import Subject, Student



def home_user (request):
    # user_id = user.id
    # user = get_object_or_404(User, pk=user_id)
    # student = get_object_or_404(Student, pk=user_id)
    return render(request, 'user/home.html', {'student': 'student'})

def student_subject (request, user_id):
    subject = get_object_or_404(Subject, pk=user_id)
    return render(request, 'journal/student_subject.html', {'subject': subject})

def student_class (request, user_id):
    subject = get_object_or_404(Subject, pk=user_id)
    return render(request, 'journal/student_class.html', {'subject': subject})

# def index(request):
#     latest_subject_list = Subject.objects.order_by('-id')
#     template = loader.get_template('journal/index.html')
#     context = RequestContext(request, {
#         'latest_subject_list': latest_subject_list,
#     })
#     return HttpResponse(template.render(context))





# def results(request, question_id):
#     response = "You're looking at the results of subject %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on subject %s." % question_id)


# class PostsListView(ListView): # представление в виде списка
#     model = Subject    

# def index(request):
#     subject_list = Subject.objects
    
#     return HttpResponse(subject_list)