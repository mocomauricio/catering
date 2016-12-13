from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from clientes.models import Cliente
from funcionarios.models import *
from extra.globals import *

# Create your views here.


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente_list.html"
    paginate_by = 30

    def get_queryset(self):
        clientes = Cliente.objects.all()
        q = self.request.GET.get('q', '')
        if q != '':
            clientes = clientes.filter( Q(nombre__icontains=q) | Q(ruc__startswith=q) | Q(razon_social__icontains=q) )

        vendedor_id=self.request.GET.get('vendedor_id','')
        if vendedor_id !='':
            clientes = clientes.filter(vendedor_id = vendedor_id)

        return clientes.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ClienteListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['vendedores'] = Funcionario.objects.all()
        context['vendedor_id'] = int(self.request.GET.get('vendedor_id','')) if (self.request.GET.get('vendedor_id','') != '') else ''
        return context

    def render_to_response(self, context, **response_kwargs):
        if 'excel' in self.request.GET.get('excel', ''): 

            lista_datos=[]
            datos = self.get_queryset()
            for dato in datos:
                lista_datos.append([
                    dato.razon_social,
                    dato.ruc,
                    dato.direccion,
                    dato.telefono,
                    dato.celular,
                    dato.email,
                    dato.vendedor.get_full_name() if dato.vendedor != None else '',
                ])

            titulos=[ 'Razon social', 'RUC', 'Direccion', 'Telefono','Celular', 'Email', 'Vendedor']
            return listview_to_excel(lista_datos,'Clientes',titulos)
        
        return super(ClienteListView, self).render_to_response(context, **response_kwargs)

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ClienteListView, self).dispatch(*args, **kwargs)

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"


def clientes_presentacion(request):
    context = RequestContext(request)
    titulo="CLIENTES"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)