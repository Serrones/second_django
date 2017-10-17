
from django.conf.urls import url
from django.views.generic import CreateView, ListView
from . import views
from  task_manager.models import Project, Task


urlpatterns = [
    url (r'^$', views.hello_page, name='home'),
    url (r'^serrones$', views.hello_serrones, name='RaD'),
    url(r'^connection$', views.connection_page, name='connection'),

    url(r'^automatic$', views.automatic_page, name='automatic'),
    url(r'^projects$', views.projects_page, name='projects'),
    url(r'^project-detail-(?P<pk>\d+)$', views.project_detail, name="project_detail"),

    url(r'^mdeveloper$', views.mdeveloper_page, name='mdeveloper'),
    url(r'^ddeveloper$', views.ddeveloper_page, name='ddeveloper'),

    url(r'^csupervisor$', views.csupervisor_page, name='csupervisor'),

    url(r'^cproject$', views.cproject_page, name='cproject'),

    url (r'^cbv_project$', CreateView.as_view(fields=['title','description','client_name'],
                                            model=Project, template_name="task_manager/cbv_project.html",
                                            success_url = 'connection'), name="cbv_project"),

    url (r'^cbv_task$', CreateView.as_view(fields=['title','description','project','importance'],
                                            model=Task, template_name="task_manager/cbv_task.html",
                                            success_url = 'connection'), name="cbv_task"),

    url (r'^cbv_project_list$', ListView.as_view(model=Project, template_name="task_manager/cbv_project_list.html"),
                                                name="cbv_project_list"), 
]
