from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    tipoDocumento = models.TextField(null=True)
    numeroDocumento = models.TextField(null=True)
    nombres = models.TextField(null=True)
    apellidos = models.TextField(null=True)
    cargo = models.TextField(null=True)
    fechaNacimiento = models.DateTimeField(null=True)
    sangreRH = models.TextField(null=True)
    correo = models.TextField(null=True)

class Conductor(models.Model):
    numeroDeLicencia = models.IntegerField(null=True)
    catergoriaLicencia = models.TextField(null=True)

class Envio(models.Model):
    fechaSolicitud = models.DateTimeField(auto_now_add=True, null=True)
    direccionEntrega = models.CharField(max_length=100, blank=True, default='', null=True)
    fechaEntregaMaxima = models.DateTimeField(null=True)

    class Meta:
        ordering = ('fechaSolicitud',)

class Pedido(models.Model):
    fechaSolicitud = models.DateTimeField(auto_now_add=True, null=True)
    direccionEntrega = models.CharField(max_length=100, blank=True, default='')
    fechaEntregaMax = models.DateTimeField(null=True)
    esPagoEnEfectivo = models.BooleanField()
    latitudGeografica = models.IntegerField(null=True)
    longitudGeografica = models.IntegerField(null=True)

class Item(models.Model):
    cantidad = models.IntegerField(null=True)

class Producto(models.Model):
    nombre = models.TextField(null=True)
    descripcion = models.TextField(null=True)
    precio = models.IntegerField(null=True)

class Inventaio(models.Model):
    unidades = models.IntegerField(null=True)

class Bodega(models.Model):
    ciudad = models.TextField(null=True)
    direccion = models.TextField(null=True)
    latitudGeografica = models.IntegerField(null=True)
    longitudGeografica = models.IntegerField(null=True)

class SolicitudAbastecimiento(models.Model):
    fechaSolicitud = models.DateTimeField(null=True)

class Operario(models.Model):
    date = models.DateTimeField(auto_now_add=True)

class UltimaUbicacion(models.Model):
    latitud = models.IntegerField(null=True)
    longitud = models.IntegerField(null=True)
    fechaSolicitud = models.DateTimeField(auto_now_add=True)

class UbicacionesRecorridas(models.Model):
    latitud = models.IntegerField(null=True)
    longitud = models.IntegerField(null=True)
    fechaSolicitud = models.DateTimeField(auto_now_add=True)

class UbicacionRuta(models.Model):
    latitud = models.IntegerField(null=True)
    longitud = models.IntegerField(null=True)