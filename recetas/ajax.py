import json
from django.http import HttpResponse
from recetas.models import *
from extra.globals import *

def get_precio_de_receta(request):
    receta_id = (request.GET['receta_id']).replace(" ","")
    print "ajax receta_id (%s)" % receta_id

    result_set = []

    if receta_id == "":
        return HttpResponse(json.dumps(result_set), 
                            content_type='application/json')


    receta = Receta.objects.get(pk=receta_id)

    result_set.append({ 
        'precio_unitario': separador_de_miles(receta.get_total()),
        'unidad_de_medida': unicode(receta.unidad_de_medida.abreviatura),
    })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')