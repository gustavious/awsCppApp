from django.db import models

# Create your models here.
from django.db import models


class Envio(models.Model):
    fechaSolicitud = models.DateTimeField(auto_now_add=True)
    direccionEntrega = models.CharField(max_length=100, blank=True, default='')
    fechaEntregaMaxima = models.DateTimeField()\

    code = models.TextField()


    class Meta:
        ordering = ('fechaSolicitud',)