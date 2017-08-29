from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^services/$', TemplateView.as_view(template_name='core/services.html'), name='services'),
    url(r'^projects/$', TemplateView.as_view(template_name='core/projects.html'), name='projects'),
    url(r'^about/$', TemplateView.as_view(template_name='core/about.html'), name='about'),
    url(r'^contact/$', views.contact, name='contact')
]
