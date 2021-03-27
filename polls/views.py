from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(" <h1>hii there ! Your django app is ready to go , bhoom! </h1>")


def detailmodify(request, question_id):
    return HttpResponse(" <h1> You are looking at question %s. </h1>" %question_id)


def results(request, question_id):
    response = "You are looking at the results of question %s ."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(" <h1> you are voting on %s . </h1>" %question_id)




# Create your views here.
