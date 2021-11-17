from django.core.management.base import BaseCommand, CommandError

import threading
import time

from gestor_topics.models import *

class Command(BaseCommand):
    help = 'Gestión de Subscripción a Brokers y Topics'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        self.stdout.write(self.style.HTTP_INFO("\nINICIANDO LA GESTION DE BROKERS Y TOPICS\n"))
        self.stdout.write(self.style.HTTP_INFO("\n Obteniendo Brokers \n"))

        # Cogemos todos los brokers para recorrerlos uno a uno
        brokers = Broker.objects.all()

        while True:
            self.stdout.write(self.style.SUCCESS("\n Total Brokers: %s" % brokers.count() ))

            