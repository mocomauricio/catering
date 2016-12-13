from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	ruc = models.CharField(max_length=20, null=True, blank=True, verbose_name="RUC/CI Nro.")
	direccion = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True)
	fecha_de_ingreso = models.DateField(null=True, blank=True)
	observaciones = models.TextField(max_length=500, null=True, blank=True)
	usuario = models.OneToOneField(User, null=True, blank=True)
	
	def get_full_name(self):
		return self.nombres + " " + self.apellidos

	def __unicode__(self):
		return unicode(self.get_full_name())