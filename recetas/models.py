from __future__ import unicode_literals

from django.db import models

# Create your models here.

PRODUCTO=0
SERVICIO=1
TIPO_ITEM=(
    (PRODUCTO,'Producto'),
    (SERVICIO,'Servicio')
)

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    #tipo = models.IntegerField(choices=TIPO_ITEM, default=PRODUCTO)
    unidad_de_medida = models.ForeignKey('ingredientes.UnidadDeMedida')

    def __unicode__(self):
        return unicode(self.nombre)

    def get_total(self):
        precio = 0
        detalles = DetalleDeReceta.objects.filter(receta_id = self.id)
        for detalle in detalles:
            precio = precio + detalle.get_subtotal()

        detalles = DetalleDeReceta2.objects.filter(receta_id = self.id)
        for detalle in detalles:
            precio = precio + detalle.get_subtotal()

        return precio 


class DetalleDeReceta(models.Model):
    class Meta:
        verbose_name = "Lista de ingrediente"
        verbose_name_plural = "Lista de ingredientes"

    receta = models.ForeignKey(Receta)
    ingrediente = models.ForeignKey('ingredientes.Ingrediente')
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)
    unidad_de_medida = models.ForeignKey('ingredientes.TablaDeConversion')

    def get_precio_unitario(self):
        return (self.ingrediente.precio_unitario*self.unidad_de_medida.factor_de_conversion)

    def get_subtotal(self):
        return (self.cantidad*self.get_precio_unitario())


class DetalleDeReceta2(models.Model):
    class Meta:
        verbose_name = "Lista de subreceta"
        verbose_name_plural = "Lista de subrecetas"

    receta = models.ForeignKey(Receta, related_name='receta_fk')
    subreceta = models.ForeignKey(Receta, related_name='subreceta_fk', verbose_name="receta")
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)

    def get_precio_unitario(self):
        return (self.subreceta.get_total())

    def get_subtotal(self):
        return (self.cantidad*self.get_precio_unitario())