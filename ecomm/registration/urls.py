from django.conf.urls import include, url
import django.contrib.auth.urls
from . import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^register/done/$', views.RegisterDoneView.as_view(),name='register_done'),
    url(r'', include(django.contrib.auth.urls)),
]
