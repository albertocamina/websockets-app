from django.shortcuts import render
from django.views.generic import *

from cruds_adminlte.crud import CRUDView

from gestor_topics.models import *

class BrokerCRUD( CRUDView ):
    model = Broker


    fields = [
        "nombre",
        "url",
        "puerto"
    ]

class TopicCRUD( CRUDView ):
    model = Topic

    fields = [
        "activo",
        "nombre",
        "broker",
        "tipo_valor",
        "usuario_en_publish"
    ]
