from dal import autocomplete
from django.db.models import Q
from recetas.models import *


class RecetaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Receta.objects.none()

        qs = Receta.objects.all()

        if self.q:
            qs = qs.filter( Q(nombre__icontains=self.q) | Q(descripcion__icontains=self.q) )

        return qs

