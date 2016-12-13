from dal import autocomplete
from django import forms
from recetas.models import *
from ingredientes.models import *

class RecetaForm(forms.ModelForm):
	class Meta:
		model = Receta
		fields = ('__all__')

	total = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="total"
	)

	def __init__(self, *args, **kwargs):
		super(RecetaForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.initial['total'] = instance.get_total()
		self.fields['total'].widget.attrs['readonly'] = True


class DetalleDeRecetaForm(forms.ModelForm):
	class Meta:
		model = DetalleDeReceta
		fields = ('__all__')
		widgets = {
			#"ingrediente":autocomplete.ModelSelect2(url='ingrediente-autocomplete'),
			"cantidad":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}

	# para eliminar los popup edit y add
	ingrediente = forms.ModelChoiceField(
		queryset=Ingrediente.objects.all(),
		widget=autocomplete.ModelSelect2(url='ingrediente-autocomplete'),
		required=True,
		label="INGREDIENTE"
	)

	precio_unitario = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="PRECIO UNITARIO"
	)

	subtotal = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="SUBTOTAL"
	)

	def __init__(self, *args, **kwargs):
		super(DetalleDeRecetaForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.initial['precio_unitario'] = instance.get_precio_unitario()
			self.initial['subtotal'] = instance.get_subtotal()
		self.fields['precio_unitario'].widget.attrs['readonly'] = True
		self.fields['subtotal'].widget.attrs['readonly'] = True


class DetalleDeReceta2Form(forms.ModelForm):
	class Meta:
		model = DetalleDeReceta2
		fields = ('__all__')
		widgets = {
			#"subreceta":autocomplete.ModelSelect2(url='receta-autocomplete'),
			"cantidad":forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		}

	# para eliminar los popup edit y add
	subreceta = forms.ModelChoiceField(
		queryset=Receta.objects.all(),
		widget=autocomplete.ModelSelect2(url='receta-autocomplete'),
		required=True,
		label="RECETA"
	)

	unidad_de_medida = forms.CharField(
		widget=forms.TextInput(attrs={'size':'9'}),
		required=False,
		label="UNIDAD DE MEDIDA"
	)

	precio_unitario = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="PRECIO UNITARIO"
	)

	subtotal = forms.CharField(
		widget=forms.TextInput(attrs={'style':'text-align:right','size':'12','class':'auto','data-a-sep':'.','data-a-dec':','}),
		required=False,
		label="SUBTOTAL"
	)

	def __init__(self, *args, **kwargs):
		super(DetalleDeReceta2Form, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.initial['unidad_de_medida'] = instance.subreceta.unidad_de_medida.abreviatura
			self.initial['precio_unitario'] = instance.get_precio_unitario()
			self.initial['subtotal'] = instance.get_subtotal()
		self.fields['unidad_de_medida'].widget.attrs['readonly'] = True
		self.fields['precio_unitario'].widget.attrs['readonly'] = True
		self.fields['subtotal'].widget.attrs['readonly'] = True


