from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello, world. You're at the polls index.")
    

def details(response, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(response, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(response, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
