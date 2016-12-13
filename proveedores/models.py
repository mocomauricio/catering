# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Proveedor(models.Model):
	class Meta:
		verbose_name = 'proveedor'
		verbose_name_plural = 'proveedores'

	razon_social = models.CharField(max_length=100)
	ruc = models.CharField(max_length=20, unique=True)
	direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name="dirección")
	telefono = models.CharField(max_length=50, null=True, blank=True, verbose_name="teléfono")
	celular = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="e-mail")

	def __unicode__(self):
		return unicode(self.razon_social)

