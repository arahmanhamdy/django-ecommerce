from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^register/done/$', TemplateView.as_view(template_name='registration/registration_done.html'),
        name='register_done')
]
