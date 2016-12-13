from django.conf.urls import patterns, include, url
from sistema.views import sistema_presentacion
from sistema.autocomplete import *
from sistema.ajax import *

urlpatterns = [

	url('usuarioautocomplete/$', 
		UsuarioAutocomplete.as_view(), 
		name='usuario-autocomplete'
	),

	url(r'^$', sistema_presentacion),

]

