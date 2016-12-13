from django.conf.urls import patterns, include, url
from recetas.autocomplete import *
from recetas.views import *
from recetas.ajax import *

urlpatterns = [
    url(
        'recetaautocomplete/$',
        RecetaAutocomplete.as_view(),
        name='receta-autocomplete',
    ),

    url('getpreciodereceta/$',get_precio_de_receta),


    url(r'^receta/(?P<pk>\d+)/detail/$', RecetaDetailView.as_view(), name='receta_det'),
    url(r'^receta/$', RecetaListView.as_view(), name='receta_lis'),
    url(r'^$', recetas_presentacion),
]

