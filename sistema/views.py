from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def sistema_presentacion(request):
	context = RequestContext(request)
	titulo="SISTEMA"
	descripcion="."
	return render_to_response('admin/presentacion.html', {'titulo':titulo,'descripcion':descripcion}, context)
