from dal import autocomplete
from django import forms
from clientes.models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')
        widgets = { 
        	"vendedor": autocomplete.ModelSelect2(url='funcionario-autocomplete'), 
        }