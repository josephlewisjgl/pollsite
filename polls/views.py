from django.shortcuts import render

# Create your views here.
from django.http import HttpRequests

def index(response):
    return HttpResponse("Hello, world. You're at the polls index.")
    