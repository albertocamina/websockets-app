from django.conf.urls import url
from django.urls.conf import include
from django.urls import path, include

from gestor_topics.views import *

broker_cruds        = BrokerCRUD()
topic_cruds         = TopicCRUD()

urlpatterns = [

    # URL de los Brokers
    url('', include( broker_cruds.get_urls() ) ),

    # URL de los Topics
    url('', include( topic_cruds.get_urls() ) )

]
