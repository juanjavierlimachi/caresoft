from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.forms import User
# Create your models here.
class Perfiles(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfil')
	materno = models.CharField(max_length=50)
	ci = models.IntegerField()
	telefono = models.IntegerField()
	def __unicode__(self):
		return self.usuario.username

class Alumnos(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfilAlumno')
	telefono = models.IntegerField()
	def __unicode__(self):
		return self.usuario.username
	
class Directores(models.Model):
	usuario = models.OneToOneField(User, unique=True, related_name='perfilDirector')
	materno = models.CharField(max_length=50)
	ci = models.IntegerField()
	telefono = models.IntegerField()
	def __unicode__(self):
		return self.usuario.username