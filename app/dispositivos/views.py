from django.shortcuts import render
from cruds_adminlte.crud import CRUDView

from dispositivos.models import *

class DispositivoCRUD( CRUDView ):
    model = Dispositivo
