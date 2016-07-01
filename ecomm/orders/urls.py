from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^order$', views.order, name='order'),
    url(r'^order/(?P<order_id>[0-9]+)$', views.view_order, name='view-order'),
    url(r'^myorders$', views.get_my_orders, name='my-orders'),
]
