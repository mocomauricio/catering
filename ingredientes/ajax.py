import json
from django.http import HttpResponse
from ingredientes.models import *
from extra.globals import *

def get_unidades_de_medida_del_ingrediente(request):
    ingrediente_id = (request.GET['ingrediente_id']).replace(" ","")

    result_set = []

    if ingrediente_id == "":
        return HttpResponse(json.dumps(result_set), 
                            content_type='application/json')

    unidades_de_medida = TablaDeConversion.objects.filter(ingrediente_id=ingrediente_id)

    for unidad_de_medida in unidades_de_medida:
        result_set.append({
            'id': unidad_de_medida.id, 
            'unidad_de_medida': unidad_de_medida.__unicode__()
        })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')


def get_precio_del_ingrediente(request):
    unidad_de_medida_id = (request.GET['unidad_de_medida_id']).replace(" ","")
    print "ajax unidad_de_medida_id (%s)" % unidad_de_medida_id

    result_set = []

    if unidad_de_medida_id == "":
        return HttpResponse(json.dumps(result_set), 
                            content_type='application/json')


    unidad_de_medida = TablaDeConversion.objects.get(pk=unidad_de_medida_id)

    result_set.append({ 
        'precio_unitario': separador_de_miles(unidad_de_medida.ingrediente.precio_unitario*unidad_de_medida.factor_de_conversion),
    })

    return HttpResponse(json.dumps(result_set), 
                        content_type='application/json')