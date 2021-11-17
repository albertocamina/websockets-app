from django.urls import path, include
from django.conf.urls import url
from dispositivos.views import DispositivoCRUD

from gestor_topics.views import *

dispositivo_crud = DispositivoCRUD()

urlpatterns = [

    # URL de los Brokers
    url('', include( dispositivo_crud.get_urls() ) ),

]
