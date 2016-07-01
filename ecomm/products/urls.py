from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<product_id>[0-9]+)/([-\w\d\_]+)/$', views.product_detail, name='product_detail'),
    url(r'^cat/(?P<category_id>[0-9]+)/([-\w\d\_]+)/$', views.category_detail, name='category_detail'),
]
