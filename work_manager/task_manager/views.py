from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task, Dev_Work_Task, Developer, Supervisor, User_Profile
from django.utils import timezone

# Create your views here.

#View for index page
def hello_page(request):
    
    return render(request, 'task_manager/index.html', {'action' : 'Save relationship'})

#View for index page
def projects_page(request):
    all_projects = Project.objects.all()
    return render(request, 'task_manager/projects.html', {'action': "Display all projects", 'all_projects': all_projects})

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'task_manager/project_detail.html', {'project': project})

#View for personal calling
def hello_serrones(request):
    return HttpResponse ("Rumo a dominação!!!")

# View for connection page
def connection_page(request):
    word = "Yep!! It's Done!!"
    return render(request, 'task_manager/connection.html', {'word': word})
