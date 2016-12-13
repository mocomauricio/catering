from dal import autocomplete
from django import forms
from recetas.models import *
from ordenes.models import *


class OrdenForm(forms.ModelForm):
	class Meta:
		model = Orden
		fields = ('__all__')
		widgets = { 
			"cliente": autocomplete.ModelSelect2(url='cliente-autocomplete'),
			"total":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}

	def __init__(self, *args, **kwargs):
		super(OrdenForm, self).__init__(*args, **kwargs)
		self.fields['total'].widget.attrs['readonly'] = True

class DetalleDeOrdenForm(forms.ModelForm):
	class Meta:
		model = DetalleDeOrden
		fields = ('__all__')
		widgets = {
			"cantidad":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
			"precio_unitario":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
			"subtotal":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}

	# para eliminar los popup edit y add
	receta = forms.ModelChoiceField(
		queryset=Receta.objects.all(),
		widget=autocomplete.ModelSelect2(url='receta-autocomplete'),
		required=True,
		label="RECETA"
	)
