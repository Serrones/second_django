from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#View for index page
def hello_page(request):
    return HttpResponse ("Hello World!!!")

#View for personal calling
def hello_serrones(request):
    return HttpResponse ("Rumo a dominação!!!")
