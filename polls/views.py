from django.shortcuts import render

# Views .py file contains the view classes for the Index, Details and Results views and the functionality for voting

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Index view displays a list of the 5 most recent questions by publication date
class IndexView(generic.ListView):
    template_name = 'polls/index.html' # load in template
    context_object_name = 'latest_question_list' # object name to display override

    # Overriding the get_queryset method to display the questions by date (top 5 most recent)
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# Details view to display the question selected in detail
class DetailsView(generic.DetailView):
    # Overriding the displayed model and the template 
    model = Question
    template_name = 'polls/details.html'

# Results view to display voting results
class ResultsView(generic.DetailView):
    # Overriding the displayed model and the template 
    model = Question
    template = 'polls/results.html'

# Vote function to add a vote to an answer choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # find the question selected or throw a 404

    # Handle the error in choices (No answer chosen)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # assign the question choice to selected and only change data with post
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else: 
        selected_choice.votes += 1 # increment vote count by one 
        selected_choice.save() # save changes 
        return HttpResponseRedirect(reverse('polls:results'), args=(question_id, )) # redirect to avoid refreshes double counting
