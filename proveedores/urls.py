from django.conf.urls import patterns, include, url
from proveedores.autocomplete import *
from proveedores.views import *
from proveedores.ajax import *

urlpatterns = [
    url(
        'proveedorautocomplete/$',
        ProveedorAutocomplete.as_view(),
        name='proveedor-autocomplete',
    ),

    url('getproveedor/$',get_proveedor),

    url(r'^proveedor/(?P<pk>\d+)/detail/$', ProveedorDetailView.as_view(), name='proveedor_det'),
    url(r'^proveedor/$', ProveedorListView.as_view(), name='proveedor_lis'),
    url(r'^$', proveedores_presentacion),
]
