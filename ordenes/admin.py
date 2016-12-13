from django.contrib import admin
from django.contrib.admin.decorators import register
from ordenes.models import *
from ordenes.forms import *


class DetalleDeOrdenInline(admin.TabularInline):
    model = DetalleDeOrden
    form = DetalleDeOrdenForm
    extra = 4


@register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    class Media:
        js = ('orden.js',)

    form = OrdenForm

    inlines = (DetalleDeOrdenInline,)

