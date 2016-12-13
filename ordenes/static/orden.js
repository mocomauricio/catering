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

            if( (vector[0] == "id_detalledeorden_set") && (vector[2] == "receta") ){
                var optionSelected = $(this).find("option:selected");
                var valueSelected  = optionSelected.val();
                console.log(valueSelected)
                if(!valueSelected){
                    $("#id_detalledeorden_set-" + vector[1] + "-precio_unitario").val("");
                    calcular_total();
                    return
                }
                $.ajax({
                    data : {'receta_id' : valueSelected },
                    url : "/admin/recetas/getpreciodereceta/",
                    type : "get",
                    success : function(data){
                        $("#id_detalledeorden_set-" + vector[1] + "-precio_unitario").val(data[0].precio_unitario);
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
    
    total_forms = $('#id_detalledeorden_set-TOTAL_FORMS').val();
    for(i=0;i<total_forms;i++){

        var cantidad = ($('#id_detalledeorden_set-'+i+'-cantidad').val()!='')?unformat(document.getElementById('id_detalledeorden_set-'+i+'-cantidad')):'0';
        var precio_unitario = ($('#id_detalledeorden_set-'+i+'-precio_unitario').val()!='')?unformat(document.getElementById('id_detalledeorden_set-'+i+'-precio_unitario')):'0';

        var subtotal = parseFloat(cantidad)*parseFloat(precio_unitario)

        if( (cantidad!='0') && (precio_unitario!='0') ){
            $('#id_detalledeorden_set-'+i+'-subtotal').val( parseFloat(subtotal).toString().replace(".",",") );
            format(document.getElementById('id_detalledeorden_set-'+i+'-subtotal'));
        } else {
            $('#id_detalledeorden_set-'+i+'-subtotal').val('');
        }

        if($('#id_detalledeorden_set-'+i+'-DELETE').is(':checked')==false){
            total_general += subtotal
        }

    }

    $('#id_total').val( parseFloat(total_general).toString().replace(".",",") );
    format(document.getElementById('id_total'));
}
