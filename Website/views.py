from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<header><h2>Welcom At home Page</h2></header>")


def contact(request):
    return HttpResponse("<header><h2>Welcom At contact Page</h2></header>")


def about(request):
    return HttpResponse("<header><h2>Welcom At about Page</h2></header>")