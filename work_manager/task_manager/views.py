from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task, Dev_Work_Task, Developer, Supervisor, User_Profile

# Create your views here.

#View for index page
def hello_page(request):
    all_projects = Project.objects.all()
    return render(request, 'task_manager/index.html', {'action': "Display all projects", 'all_projects': all_projects})
#View for personal calling
def hello_serrones(request):
    return HttpResponse ("Rumo a dominação!!!")

# View for connection page
def connection_page(request):
    word = "Yep!! It's Done!!"
    return render(request, 'task_manager/connection.html', {'word': word})
