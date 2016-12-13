from django.contrib import admin
from django.contrib.admin.decorators import register
from clientes.models import Cliente
from clientes.forms import ClienteForm

@register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('razon_social', 'ruc')
    form = ClienteForm
