from django.db import models

from dispositivos.choices import *

class Dispositivo( models.Model ):
    nombre      = models.CharField( max_length=1000, blank=False, null=False )
    tipo        = models.CharField( choices=TIPOS_DISPOSITIVO, max_length=1000, blank=False, null=False )
    ip          = models.GenericIPAddressField( blank=False, null=False )
    disponible  = models.BooleanField( default=True, null=False, blank=False )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name        = "Dispositivo"
        verbose_name_plural = "Dispositivos"
        ordering            = (
            "nombre",
        )
