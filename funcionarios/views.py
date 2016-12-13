from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from funcionarios.models import Funcionario


class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "funcionario_list.html"

    def get_queryset(self):
        funcionarios = Funcionario.objects.all()

        q = self.request.GET.get('q', '')
        if q != '':
            funcionarios = funcionarios.filter( Q(nombres__icontains=q) | Q(apellidos__icontains=q) )

        return funcionarios


    def get_context_data(self, **kwargs):
        context = super(FuncionarioListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "funcionario_detail.html"

def funcionarios_presentacion(request):
    context = RequestContext(request)
    titulo="FUNCIONARIOS"
    descripcion=".."
    return render_to_response('admin/presentacion.html', {'titulo': titulo, 'descripcion': descripcion}, context)