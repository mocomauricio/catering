from django.db import models
from datetime import date

# Create your models here.
PENDIENTE=0
PROCESADO=1
ENTREGADO=2
ESTADOS_ORDENES=(
    (PENDIENTE,'Pendiente'),
    (PROCESADO,'Procesado'),
    (ENTREGADO,'Entregado')
)

class Orden(models.Model):
    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

    cliente = models.ForeignKey('clientes.Cliente')
    fecha = models.DateField(default=date.today)
    estado = models.IntegerField(default=PENDIENTE, choices=ESTADOS_ORDENES, editable=False)
    total = models.DecimalField(max_digits=15, decimal_places=2)

    def __unicode__(self):
        return unicode("Orden Nro.: " + str(self.id))


class DetalleDeOrden(models.Model):
    class Meta:
        verbose_name = "Detalle de la orden"
        verbose_name_plural = "Detalle de la orden"

    orden = models.ForeignKey(Orden)
    receta = models.ForeignKey('recetas.Receta')
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)

    def get_subtotal(self):
        return (self.cantidad*self.get_precio_unitario())

