from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_shiku(request):
    return HttpResponse('Hello! My name is shiku')
