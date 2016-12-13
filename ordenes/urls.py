from django.conf.urls import patterns, include, url
from ordenes.autocomplete import *
from ordenes.views import *
from ordenes.ajax import *

urlpatterns = [
    

    url(r'^orden/(?P<pk>\d+)/detail/$', OrdenDetailView.as_view(), name='orden_det'),
    url(r'^orden/$', OrdenListView.as_view(), name='orden_lis'),

    url(r'^$', ordenes_presentacion),
]

