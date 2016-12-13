from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from recetas.models import *
from extra.globals import *

# Create your views here.
class RecetaListView(ListView):
    model = Receta
    template_name = "receta_list.html"
    paginate_by = 30

    def get_queryset(self):
        recetas = Receta.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            recetas = recetas.filter( Q(nombre__icontains=q) | Q(descripcion__icontains=q) )
        return recetas

    def get_context_data(self, **kwargs):
        context = super(RecetaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''): 

            lista_datos=[]
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.nombre,
                    #dato.get_unidad_de_medida().nombre,
                    separador_de_miles(dato.get_total()),
                ])

            titulos=[ 
                'Nombre',
                #'Unidad de medida', 
                'Precio unitario', 
            ]
            return listview_to_excel(lista_datos,'Recetas',titulos)
        
        return super(RecetaListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(RecetaListView, self).dispatch(*args, **kwargs)

class RecetaDetailView(DetailView):
    model = Receta
    template_name = "receta_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RecetaDetailView, self).get_context_data(**kwargs)
        context['detalle_de_ingredientes'] = DetalleDeReceta.objects.filter(receta_id=self.object.id)
        context['detalle_de_subrecetas'] = DetalleDeReceta2.objects.filter(receta_id=self.object.id)
        return context

def recetas_presentacion(request):
    context = RequestContext(request)
    titulo="RECETAS"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)