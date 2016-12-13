from dal import autocomplete
from django import forms
from ingredientes.models import *

class IngredienteForm(forms.ModelForm):
	class Meta:
		model = Ingrediente
		fields = ('__all__')
		widgets = { 
			"categoria": autocomplete.ModelSelect2(url='categoriadeingrediente-autocomplete'),
			"proveedores": autocomplete.ModelSelect2Multiple(url='proveedor-autocomplete'),
			"precio_unitario":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}

	unidad_de_medida = forms.ModelChoiceField(
		queryset=UnidadDeMedida.objects.all(),
		#widget=autocomplete.ModelSelect2(url='unidaddemedida-autocomplete'),
		required=True,
		label="Unidad de medida"
	)


	def __init__(self, *args, **kwargs):
		super(IngredienteForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.initial['unidad_de_medida'] = instance.get_unidad_de_medida()


class TablaDeConversionForm(forms.ModelForm):
	class Meta:
		model = TablaDeConversion
		fields = ('__all__')
		widgets = {
			"factor_de_conversion":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
	   	}

	unidad_de_medida = forms.ModelChoiceField(
		queryset=UnidadDeMedida.objects.all(),
		#widget=autocomplete.ModelSelect2(url='unidaddemedida-autocomplete'),
		required=True,
		label="Unidad de medida"
	)
