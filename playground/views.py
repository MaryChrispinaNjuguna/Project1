from django.shortcuts import render
from django.http import HTTPresponse
# Create your views here.
def hello(request):
    return HTTPresponse('Hello World!')
