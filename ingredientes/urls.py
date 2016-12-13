from django.conf.urls import patterns, include, url
from ingredientes.autocomplete import *
from ingredientes.views import *
from ingredientes.ajax import *

urlpatterns = [
    url(
        'unidaddemedidaautocomplete/$',
        UnidadDeMedidaAutocomplete.as_view(),
        name='unidaddemedida-autocomplete',
    ),

    url(
        'categoriadeingredienteautocomplete/$',
        CategoriaDeIngredienteAutocomplete.as_view(),
        name='categoriadeingrediente-autocomplete',
    ),

    url(
        'ingredienteautocomplete/$',
        IngredienteAutocomplete.as_view(),
        name='ingrediente-autocomplete',
    ),

    url('getunidadesdemedidadelingrediente/$',get_unidades_de_medida_del_ingrediente),
    url('getpreciodelingrediente/$',get_precio_del_ingrediente),

    url(r'^unidaddemedida/$', UnidadDeMedidaListView.as_view(), name='unidaddemedida_lis'),

    url(r'^categoriadeingrediente/$', CategoriaDeIngredienteListView.as_view(), name='categoriadeingrediente_lis'),
    
    url(r'^ingrediente/$', IngredienteListView.as_view(), name='ingrediente_lis'),
    url(r'^ingrediente/(?P<pk>\d+)/detail/$', IngredienteDetailView.as_view(), name='ingrediente_det'),

    url(r'^$', ingredientes_presentacion),
]

