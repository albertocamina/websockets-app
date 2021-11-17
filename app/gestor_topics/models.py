from django.db import models
from django.contrib.auth import get_user_model

from gestor_topics.choices import *

class Broker( models.Model ):
    estado          = models.BooleanField( default=False, blank=False, null=False )
    nombre          = models.CharField( max_length=500, blank=False, null=False )
    url             = models.CharField( max_length=500, blank=False, null=True ) 
    puerto          = models.CharField( max_length=4, blank=False, null=True )

    class Meta:
        verbose_name            = "Broker"
        verbose_name_plural     = "Brokers"
        ordering                = ( "nombre", )

    def __str__(self):
        return "%s - %s:%s" % ( self.nombre, self.url, self.puerto )

class Topic( models.Model ):
    estado                  = models.BooleanField( default=False, blank=False, null=False )
    activo                  = models.BooleanField( default=True, blank=False, null=False )
    nombre                  = models.CharField( max_length=500, blank=False, null=False )
    broker                  = models.ForeignKey("Broker", related_name="topics", on_delete=models.PROTECT, null=False, blank=False )

    ## Guarda el tipo de valor del topic ## 
    tipo_valor              = models.CharField( max_length=500, choices=TIPO_VALOR_TOPICS, blank=False, null=True )

    # Guarda el usuario que hizo el publish #
    usuario_en_publish      = models.BooleanField( default=False, blank=False, null=False )

    class Meta:
        verbose_name            = "Topic"
        verbose_name_plural     = "Topics"
        ordering                = ( "nombre", )

class ValorTopic( models.Model ): 
    creado                  = models.DateTimeField( auto_created=True, null=False )
    usuario                 = models.ForeignKey(get_user_model(), related_name="valores_publicados", on_delete=models.PROTECT, null=False, blank=False )
    topic                   = models.ForeignKey("Topic", related_name="valores", on_delete=models.PROTECT, null=False, blank=False )

    charfield               = models.CharField( max_length=5000, blank=True, null=True )
    decimalfield            = models.DecimalField( max_digits=10, decimal_places=2, blank=True, null=True )
    floatfield              = models.FloatField( blank=True, null=True )
    integerfield            = models.IntegerField( blank=True, null=True )
    positiveintegerfield    = models.PositiveIntegerField( blank=True, null=True )
    bigintegerfield         = models.BigIntegerField( blank=True, null=True )
    smallintegerfield       = models.SmallIntegerField( blank=True, null=True )
    booleanfield            = models.BooleanField( blank=True, null=True )

    class Meta:
        verbose_name            = "Valor de Topic"
        verbose_name_plural     = "Valores de Topics"
        ordering                = ( "-creado", )

    
