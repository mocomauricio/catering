from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from ingredientes.models import *
from extra.globals import *
# Create your views here.

class UnidadDeMedidaListView(ListView):
    model = UnidadDeMedida
    template_name = "unidaddemedida_list.html"
    paginate_by = 30

    def get_queryset(self):
        unidadesdemedidas = UnidadDeMedida.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            unidadesdemedidas = unidadesdemedidas.filter(nombre__icontains=q)

        return unidadesdemedidas

    def get_context_data(self, **kwargs):
        context = super(UnidadDeMedidaListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        return context



class CategoriaDeIngredienteListView(ListView):
    model = CategoriaDeIngrediente
    template_name = "categoriadeingrediente_list.html"
    paginate_by = 30

    def get_queryset(self):
        categoriasdeingredientes = CategoriaDeIngrediente.objects.all().order_by('nombre_completo')

        q = self.request.GET.get('q', '')
        if q != '':
            categoriasdeingredientes = categoriasdeingredientes.filter(Q(nombre_completo__icontains=q))
        return categoriasdeingredientes

    def get_context_data(self, **kwargs):
        context = super(CategoriaDeIngredienteListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        return context



class IngredienteListView(ListView):
    model = Ingrediente
    template_name = "ingrediente_list.html"
    paginate_by = 30

    def get_queryset(self):
        ingredientes = Ingrediente.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            ingredientes = ingredientes.filter( Q(descripcion__icontains=q) | Q(id__startswith=q) )
        return ingredientes

    def get_context_data(self, **kwargs):
        context = super(IngredienteListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''): 

            lista_datos=[]
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.codigo,
                    dato.descripcion,
                    dato.marca,
                    dato.get_iva_display(),
                    dato.categoria.nombre,
                    dato.stock_actual,
                    dato.get_unidad_de_medida().nombre,
                    separador_de_miles(dato.precio_unitario),
                ])

            titulos=[ 
                'Codigo',
                'Descripcion',  
                'Marca',
                'IVA',
                'Categoria', 
                'Stock actual',
                'Unidad de medida', 
                'Precio unitario', 
            ]
            return listview_to_excel(lista_datos,'Ingredientes',titulos)
        
        return super(IngredienteListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(IngredienteListView, self).dispatch(*args, **kwargs)

class IngredienteDetailView(DetailView):
    model = Ingrediente
    template_name = "ingrediente_detail.html"

    def get_context_data(self, **kwargs):
        context = super(IngredienteDetailView, self).get_context_data(**kwargs)
        return context

def ingredientes_presentacion(request):
    context = RequestContext(request)
    titulo="INGREDIENTES"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)