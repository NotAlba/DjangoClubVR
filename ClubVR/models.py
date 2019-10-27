import datetime

from django.db import models
from django.utils import timezone


class Aula(models.Model):
	nombreAula = models.CharField(max_length=50)
	ubicacion = models.CharField(max_length=50)
	def __str__(self):
		return self.nombreAula

class Gafas(models.Model):
	id_aula = models.ForeignKey(Aula,on_delete=models.CASCADE)
	ordenador = models.CharField(max_length=2)
	tipo = models.CharField(max_length=10)
	def __str__(self):
		return self.tipo

class Juego(models.Model):
	nombreJuego = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombreJuego



class Usuario(models.Model):

	nombreUsuario = models.CharField(max_length=100)
	apellidoUsuario = models.CharField(max_length=200)
	edadUsuario = models.CharField(max_length=100)
	mailUsuario = models.CharField(max_length=100)
	telefonoUsuario = models.IntegerField(999999999)
	def __str__(self):
		return self.nombreUsuario

class Reserva(models.Model):
	id_gafas = models.ForeignKey(Gafas,on_delete=models.CASCADE)
	id_juego = models.ForeignKey(Juego,on_delete=models.CASCADE)
	id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	fecha_inicio = models.DateTimeField('Fecha de incio de la reserva')
	fecha_fin = models.DateTimeField('Fecha de fin de la reserva')

