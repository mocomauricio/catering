from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Q

from clientes.models import *
from ordenes.models import *
from extra.globals import *

# Create your views here.
class OrdenListView(ListView):
    model = Orden
    template_name = "orden_list.html"
    paginate_by = 30

    def get_queryset(self):
        ordenes = Orden.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            ordenes = ordenes.filter( id__istartswith=q )

        cliente_id = self.request.GET.get('cliente_id', '')
        if cliente_id != '':
            ordenes = ordenes.filter(cliente_id=cliente_id)

        estado = self.request.GET.get('estado', '0')
        if estado != 'TODO':
            ordenes = ordenes.filter(estado=estado)

        fecha = self.request.GET.get('fecha', '')
        if fecha != '':
            vector = fecha.split("/")
            fecha = vector[2] + "-" + vector[1] + "-" + vector[0]
            ordenes = ordenes.filter(fecha=fecha)


        return ordenes.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super(OrdenListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','')
        context['clientes'] = Cliente.objects.all()
        context['cliente_id'] = int(self.request.GET.get('cliente_id', '')) if (self.request.GET.get('cliente_id', '') != '') else ''
        context['estado'] = self.request.GET.get('estado','0')
        context['fecha'] = self.request.GET.get('fecha','')
        return context

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(OrdenListView, self).dispatch(*args, **kwargs)

class OrdenDetailView(DetailView):
    model = Orden
    template_name = "orden_detail.html"

    def get_context_data(self, **kwargs):
        context = super(OrdenDetailView, self).get_context_data(**kwargs)
        context['detalles'] = DetalleDeOrden.objects.filter(orden_id=self.object.id)
        return context

def ordenes_presentacion(request):
    context = RequestContext(request)
    titulo="ORDENES"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)