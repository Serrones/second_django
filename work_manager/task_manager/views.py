from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Task, Dev_Work_Task, Developer, Supervisor, User_Profile
from django.utils import timezone
from django import forms
from django.core.urlresolvers import reverse

# Create your views here.

#View for index page
def hello_page(request):
    return render(request, 'task_manager/index.html', {'action' : 'Home Page'})

#View for automatic saving data -- with a model
def automatic_page(request):
    new_project = Project(title="Saving data with a model",
    description="We input data directly in the view.function",
    client_name="Mr. Sadahm")
    new_project.save()
    return render(request, 'task_manager/automatic.html', {'action':'Save datas of model'})

#View for projects list
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



#View for create_developer with html form
def mdeveloper_page(request):
    error = False # If form has posted
    if request.POST: # This line checks if the data was sent in POST. If so, this means that the form has been submitted and we should treat it.
        if 'name' in request.POST: # This line checks whether a given data named name exists in the POST variables.
            name = request.POST.get('name', '') # This line is used to retrieve the value in the POST dictionary. Normally, we perform filters to recover the data to avoid false data, but it would have required many lines of code.
        else:
            error=True
        if 'login' in request.POST:
            login = request.POST.get('login', '')
        else:
            error=True
        if 'password' in request.POST:
                password = request.POST.get('password', '')
        else:
            error=True
        if 'supervisor' in request.POST:
            supervisor_id = request.POST.get('supervisor', '')
        else:
            error=True
        if not error: # We must get the supervisor
                supervisor = Supervisor.objects.get(id = supervisor_id)
                new_dev = Developer(name=name, login=login, password=password, gerente=supervisor)
                new_dev.save()
                return HttpResponse("Developer added")
        else:
            return HttpResponse("An error has occured")
    else:
        supervisors_list = Supervisor.objects.all()
        return render(request, 'task_manager/mdeveloper.html', {'supervisors_list':supervisors_list})

error_name = {
                'required': 'You must type a name !',
                'invalid': 'Wrong format.'
                }

class Form_inscription(forms.Form):
    """ This line creates the form with four fields. It is an object that
    inherits from forms.Form. It contains attributes that define the form
    fields."""
    name = forms.CharField(label="Name", max_length=30, error_messages=error_name, initial="New")
    login = forms.CharField(label="Login", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_bis = forms.CharField(label = "Password", widget = forms.PasswordInput)
    supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all(),
                                        initial=Supervisor.objects.all()[:1].get().id)

    def clean(self):
        cleaned_data = super(Form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')
        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are not identical.")
        return self.cleaned_data

# View for create_developer with Django form
def ddeveloper_page(request):
    if request.POST:
        form = Form_inscription(request.POST)
        """ If the form has been posted, we create the variable that will
        contain our form filled with data sent by POST form."""
        if form.is_valid():
            """ This line checks that the data sent by the user is consistent
            with the field that has been defined in the form. """
            name = form.cleaned_data['name']
            """ This line is used to retrieve the value sent by the client. The
            collected data is filtered by the clean() method that we will see
            later. This way to recover data provides secure data."""
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            supervisor = form.cleaned_data['supervisor']
            """ In this line, the supervisor variable is of the Supervisor
            type, that is to say that the returned data by the cleaned_data
            dictionary will directly be a model."""
            new_developer = Developer(name=name, login=login,
                password=password, email="", gerente=supervisor)
            new_developer.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'task_manager/ddeveloper.html',{'form' : form})
            """ To send forms to the template, just send it like any other
            variable. We send it in case the form is not valid in order
            to display user errors:"""
    else:
        form = Form_inscription()
        """ In this case, the user does not yet display the form, it
        instantiates with no data inside."""
        return render(request, 'task_manager/ddeveloper.html', {'form': form})

def csupervisor_page(request):
    if len(request.POST) > 0:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # If the form is valid, we store the data in a model record in the form.
            return HttpResponseRedirect(reverse('home'))
            # This line is used to redirect to the specified URL. We use the reverse() function to get the URL from its name defines urls.py.
        else:
            return render(request, 'task_manager/csupervisor.html', {'form': form})
    else:
        form = Form_supervisor()
        return render(request, 'task_manager/csupervisor.html', {'form': form})

class Form_supervisor(forms.ModelForm):
    # Here we create a class that inherits from ModelForm.
    class Meta:
        """ We extend the Meta class of the ModelForm. It is this class that
        will allow us to define the properties of ModelForm."""
        model = Supervisor # We define the model that should be based on the form.
        exclude = ('date_created', 'last_connection', 'born_date', 'phone')
        """ We exclude certain fields of this form. It would also have been
        possible to do the opposite. That is to say with the fields property,
        we have defined the desired fields in the form."""

class Form_project_create(forms.Form):
    title = forms.CharField(label="Title", max_length=30)
    description = forms.CharField(widget= forms.Textarea(attrs={'rows':5, 'cols': 100,}))
    client_name = forms.CharField(label="Client", max_length=50)

def cproject_page(request):
    if request.POST:
        form = Form_project_create(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            client_name = form.cleaned_data['client_name']
            new_project = Project(title=title, description=description, client_name=client_name)
            new_project.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'task_manager/create_project.html', {'form': form})
    else:
        form = Form_project_create()
        return render(request, 'task_manager/create_project.html', {'form' : form})
