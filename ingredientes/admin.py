from django.contrib import admin
from django.contrib.admin.decorators import register
from ingredientes.models import *
from ingredientes.forms import *


@register(UnidadDeMedida)
class UnidadDeMedidaAdmin(admin.ModelAdmin):
    pass

@register(CategoriaDeIngrediente)
class CategoriaDeIngredienteAdmin(admin.ModelAdmin):
    pass

class TablaDeConversionInline(admin.TabularInline):
    model = TablaDeConversion
    form = TablaDeConversionForm
    extra = 4


@register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    class Media:
        js = ('ingrediente.js',)

    form = IngredienteForm

    inlines = (TablaDeConversionInline,)

