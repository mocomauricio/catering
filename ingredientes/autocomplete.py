from dal import autocomplete
from django.db.models import Q
from ingredientes.models import *



class UnidadDeMedidaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return UnidadDeMedida.objects.none()

        qs = UnidadDeMedida.objects.all()

        if self.q:
            qs = qs.filter( Q(nombre__icontains=self.q) | Q(abreviatura__istartswith=self.q) )

        return qs


class CategoriaDeIngredienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return CategoriaDeIngrediente.objects.none()

        qs = CategoriaDeIngrediente.objects.all()

        if self.q:
            qs = qs.filter(nombre__icontains=self.q)

        return qs
        

class IngredienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Ingrediente.objects.none()

        qs = Ingrediente.objects.all()

        if self.q:
            qs = qs.filter( Q(codigo__istartswith=self.q) | Q(descripcion__icontains=self.q) )

        return qs


