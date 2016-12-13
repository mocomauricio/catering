# -*- coding: utf-8 -*-

from django.db import models
from django.apps import apps

class UnidadDeMedida(models.Model):
    class Meta:
        verbose_name = "unidad de medida"
        verbose_name_plural = "unidades de medida"

    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, verbose_name="Símbolo")

    def __str__(self):
        return self.nombre


class CategoriaDeIngrediente(models.Model):
    class Meta:
        verbose_name = "categoría de ingredientes"
        verbose_name_plural = "categorías de ingredientes"

    nombre = models.CharField(max_length=100, unique=True)
    nombre_completo = models.CharField(max_length=500, editable=False, null=True)
    categoria_padre = models.ForeignKey("self", related_name='categoria_fk', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.categoria_padre != None:
            self.nombre_completo = self.categoria_padre.nombre_completo + " " + self.nombre
        else:
            self.nombre_completo = self.nombre

        super(CategoriaDeIngrediente, self).save(*args, **kwargs)

        categorias_hijas = CategoriaDeIngrediente.objects.filter(categoria_padre=self)
        for categoria_hija in categorias_hijas:
            categoria_hija.save()

    def __str__(self):
        return self.nombre_completo


IVA = (
    (10, 'IVA 10%'), 
    (5, 'IVA 5%'), 
    (0, 'EXENTA')
)
class Ingrediente(models.Model):
    class Meta:
        verbose_name_plural = "ingredientes"

    codigo = models.CharField(max_length=10, unique=True, verbose_name="código")
    descripcion = models.CharField(max_length=150, verbose_name="descripción")
    marca = models.CharField(max_length=100, null=True, blank=True)
    iva = models.IntegerField("IVA", choices=IVA, default=10)    
    categoria = models.ForeignKey(CategoriaDeIngrediente, verbose_name="categoría")
    proveedores = models.ManyToManyField('proveedores.Proveedor', blank=True)  
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2)
    stock_actual = models.DecimalField(max_digits=15, decimal_places=2, default=0, editable=False)

    def __unicode__(self):
        return unicode(self.descripcion + " - " + self.marca)

    def get_unidad_de_medida(self):
        return (TablaDeConversion.objects.filter(ingrediente_id = self.id)[0]).unidad_de_medida

    """
    def actualizar_stock(self):
        cantidad = 0

        detalles_altas = apps.get_model("depositos","DetalleAlta").objects.filter(ingrediente_id = self.id)
        for detalle in detalles_altas:
            cantidad = cantidad + detalle.cantidad

        detalles_bajas = apps.get_model("depositos","DetalleBaja").objects.filter(ingrediente_id = self.id)
        for detalle in detalles_bajas:
            cantidad = cantidad - detalle.cantidad

        detalles_retiros = apps.get_model("depositos","DetalleRetiro").objects.filter(ingrediente_id = self.id)
        for detalle in detalles_retiros:
            cantidad = cantidad - detalle.cantidad

        detalles_devoluciones = apps.get_model("depositos","DetalleDevolucion").objects.filter(detalle_retiro__ingrediente__id = self.id)
        for detalle in detalles_devoluciones:
            cantidad = cantidad + detalle.cantidad

        self.stock_actual = cantidad
        self.save()
    """


class TablaDeConversion(models.Model):
    class Meta:
        verbose_name = 'Otra unidad de medida'
        verbose_name_plural = 'Otras unidades de medida'

    ingrediente = models.ForeignKey(Ingrediente)
    unidad_de_medida = models.ForeignKey(UnidadDeMedida)
    factor_de_conversion = models.DecimalField(max_digits=15, decimal_places=2, help_text="Numero a multiplicar para convertir en la unidad de medida principal")

    def __unicode__(self):
        return self.unidad_de_medida.abreviatura 
