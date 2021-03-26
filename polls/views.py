from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(" <h1>hii there ! Your django app is ready to go , bhoom! </h1>")




# Create your views here.
