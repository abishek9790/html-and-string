from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def funa(request):
    return HttpResponse("app1 function 1")
def funb(request):
    return HttpResponse("app1 function 2")
