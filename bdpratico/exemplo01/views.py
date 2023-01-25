from django.shortcuts import render
##from . import views
from django.http import HttpResponse
def index(request):
    return HttpResponse("EXEMPLO 01.")