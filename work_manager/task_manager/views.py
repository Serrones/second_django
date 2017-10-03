from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#View for index page
def hello_page(request):
    word = "Hello World!"
    years_old = 19
    capital = ['paris', 'new york', 'london']
    return render (request, 'index.html', {'word': word, 'years': years_old, 'cap': capital})

#View for personal calling
def hello_serrones(request):
    return HttpResponse ("Rumo a dominação!!!")
