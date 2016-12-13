(function($) {
    $(document).ready(function() {

        // recalcular totales al marcar o desmarcar algo como borrado
        $('form input[type=checkbox]').click(function(e) {
            calcular_total();
        });

        // recalcular totales al borrar un receta de un detalle no guardador (con botoncito 'x')
        $('.inline-deletelink').click(function() {
            calcular_total();
        });

        // calcular totales al editar campos numericos
        $('.auto').keyup(function(){
            calcular_total();
        });

        // al cambiar un select en el inline
        $('select').change(function(){
            vector = $(this).attr("id").split("-");
            if( (vector[0] == "id_detalledereceta_set") && (vector[2] == "ingrediente") ){

                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                if(!valueSelected){
                    $("#id_detalledereceta_set-" + vector[1] + "-unidad_de_medida option").remove();
                    $("#id_detalledereceta_set-" + vector[1] + "-unidad_de_medida").append("<option value=\"\" selected=\"selected\">---------</option>");
                    $("#id_detalledereceta_set-" + vector[1] + "-precio_unitario").val("");
                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'ingrediente_id' : valueSelected },
                    url : "/admin/ingredientes/getunidadesdemedidadelingrediente",
                    type : "get",
                    success : function(data){
                        $("#id_detalledereceta_set-" + vector[1] + "-unidad_de_medida option").remove();
                        $("#id_detalledereceta_set-" + vector[1] + "-unidad_de_medida").append("<option value=\"\" selected=\"selected\">---------</option>");
                        for (var i = 0; i < data.length; i++) {
                            $("#id_detalledereceta_set-" + vector[1] + "-unidad_de_medida").append('<option value='+ data[i].id +'>'+ data[i].unidad_de_medida +'</option>');
                        }
                    }
                });
            }

            if( (vector[0] == "id_detalledereceta_set") && (vector[2] == "unidad_de_medida") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                console.log(valueSelected)
                if(!valueSelected){
                    $("#id_detalledereceta_set-" + vector[1] + "-precio_unitario").val("");
                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'unidad_de_medida_id' : valueSelected },
                    url : "/admin/ingredientes/getpreciodelingrediente/",
                    type : "get",
                    success : function(data){
                        $("#id_detalledereceta_set-" + vector[1] + "-precio_unitario").val(data[0].precio_unitario);
                        calcular_total();
                    }
                });
            }


            if( (vector[0] == "id_receta_fk") && (vector[2] == "subreceta") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                console.log(valueSelected)
                if(!valueSelected){
                    $("#id_receta_fk-" + vector[1] + "-precio_unitario").val("");
                    $("#id_receta_fk-" + vector[1] + "-unidad_de_medida").val("");
                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'receta_id' : valueSelected },
                    url : "/admin/recetas/getpreciodereceta/",
                    type : "get",
                    success : function(data){
                        $("#id_receta_fk-" + vector[1] + "-precio_unitario").val(data[0].precio_unitario);
                        $("#id_receta_fk-" + vector[1] + "-unidad_de_medida").val(data[0].unidad_de_medida);
                        calcular_total();
                    }
                });
            }


        });

    });


})(django.jQuery);

/*
    calculo de los totales
*/
function calcular_total(){
    var total_general = 0;
    
    total_forms = $('#id_detalledereceta_set-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var cantidad = ($('#id_detalledereceta_set-'+i+'-cantidad').val()!='')?unformat(document.getElementById('id_detalledereceta_set-'+i+'-cantidad')):'0';
        var precio_unitario = ($('#id_detalledereceta_set-'+i+'-precio_unitario').val()!='')?unformat(document.getElementById('id_detalledereceta_set-'+i+'-precio_unitario')):'0';

        var subtotal = parseFloat(cantidad)*parseFloat(precio_unitario)

        if( (cantidad!='0') && (precio_unitario!='0') ){
            $('#id_detalledereceta_set-'+i+'-subtotal').val( parseFloat(subtotal).toString().replace(".",",") );
            format(document.getElementById('id_detalledereceta_set-'+i+'-subtotal'));
        } else {
            $('#id_detalledereceta_set-'+i+'-subtotal').val('');
        }

        if($('#id_detalledereceta_set-'+i+'-DELETE').is(':checked')==false){
            total_general += subtotal
        }

    }

    total_forms = $('#id_receta_fk-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var cantidad = ($('#id_receta_fk-'+i+'-cantidad').val()!='')?unformat(document.getElementById('id_receta_fk-'+i+'-cantidad')):'0';
        var precio_unitario = ($('#id_receta_fk-'+i+'-precio_unitario').val()!='')?unformat(document.getElementById('id_receta_fk-'+i+'-precio_unitario')):'0';

        var subtotal = parseFloat(cantidad)*parseFloat(precio_unitario)

        if( (cantidad!='0') && (precio_unitario!='0') ){
            $('#id_receta_fk-'+i+'-subtotal').val( parseFloat(subtotal).toString().replace(".",",") );
            format(document.getElementById('id_receta_fk-'+i+'-subtotal'));
        } else {
            $('#id_receta_fk-'+i+'-subtotal').val('');
        }

        if($('#id_receta_fk-'+i+'-DELETE').is(':checked')==false){
            total_general += subtotal
        }

    }

    $('#id_total').val( parseFloat(total_general).toString().replace(".",",") );
    format(document.getElementById('id_total'));
}
