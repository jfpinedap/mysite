from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def owner_old(request):
    print(request.COOKIES)
    response = HttpResponse("Hello, world. dab10c50 is the polls index.")
    response.set_cookie('dj4e_cookie', 'dcf9082a', max_age=1000)
    return response

def owner(request):
    # print('owner request: ', request.COOKIES)
    # num_visits = request.session.get('num_visits_i', 0) + 1
    # request.session['num_visits_i'] = num_visits
    # if num_visits > 4 : del(request.session['num_visits_i'])
    response = HttpResponse("Hello, world. dcf9082a .")
    # response.set_cookie('dj4e_cookie', 'dcf9082a', max_age=1000)
    return response
