import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
django.setup()

from scrum.models import Epica, Tarea, Sprint
from django.contrib.auth.models import User


def populate():

    epicas = [
        {'nombre':'','descripcion':'','criterios_aceptacion':'','estado':''}
    ]

    autores = [
        {'nombre': 'Gabriel García Márquez', 'fecha_nacimiento': '1927-03-06'},
        {'nombre': 'J.K. Rowling', 'fecha_nacimiento': '1965-07-31'},
        # Agrega más autores según sea necesario
    ]
    
    for autor_data in autores:
        autor = Autor(**autor_data)
        autor.save()  # Guarda cada autor en la base de datos
        print(f'Autor {autor.nombre} agregado.')

if __name__ == '__main__':
    populate()