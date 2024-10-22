import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ActividadGrupal.settings')
django.setup()

from django.core.management.base import BaseCommand #Comandos de django para usarlo como el shell
from scrum.models import Epica, Tarea, Sprint #Los modelos del scrum
from django.contrib.auth.models import User 

def vaciar_db():
    Sprint.objects.all().delete()
    Tarea.objects.all().delete()
    Epica.objects.all().delete()
    print('BASE DE DATOS VACIADA CORRECTAMENTE')

if __name__ == '__main__':
    vaciar_db()