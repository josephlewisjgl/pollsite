from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)
    

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'polls/details.html', context)

def results(response, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(response, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
