
from django.conf.urls import url
from . import views



urlpatterns = [
    url (r'^$', views.hello_page, name='home'),
    url (r'^serrones$', views.hello_serrones, name='RaD'),
    url(r'^connection$', views.connection_page, name='connection'),
]
