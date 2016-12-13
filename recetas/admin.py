from django.contrib import admin
from django.contrib.admin.decorators import register
from recetas.models import *
from recetas.forms import *

# Register your models here.
class DetalleDeRecetaInline(admin.TabularInline):
	model = DetalleDeReceta
	form = DetalleDeRecetaForm
	extra = 3

class DetalleDeReceta2Inline(admin.TabularInline):
	model = DetalleDeReceta2
	fk_name = 'receta'
	form = DetalleDeReceta2Form
	extra = 3

@register(Receta)
class RecetaAdmin(admin.ModelAdmin):
	class Media:
		js = ('receta.js',)
	inlines = (DetalleDeRecetaInline, DetalleDeReceta2Inline,)
	form = RecetaForm
	list_display = ('nombre', 'unidad_de_medida')