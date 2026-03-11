from django.db.models import F
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        # exemplo do objeto post: <QueryDict: {'csrfmiddlewaretoken': ['AbC123xyz'], 'choice': ['1']}>
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # sempre deve retornar um HttpResponseRedirect depois de lidar com dados POST
        # para evitar que os dados sejam postados duas vezes se o usuário clicar no botão Voltar
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        # reverse cria a URL de acordo com a view e os argumentos passados, exemplo: /polls/5/results/