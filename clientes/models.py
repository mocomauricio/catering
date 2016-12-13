# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Cliente(models.Model):
    razon_social = models.CharField(max_length=100, verbose_name="razón social")
    ruc = models.CharField(max_length=20, verbose_name="RUC", unique=True)
    direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name="dirección")
    celular = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True, verbose_name="teléfono")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="e-mail")
    vendedor = models.ForeignKey('funcionarios.Funcionario', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.razon_social)
