import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ActividadGrupal.settings')
django.setup()

from scrum.models import Epica, Tarea, Sprint
from django.contrib.auth.models import User


def populate():

    epicas = [
          {
        'nombre': 'Desarrollo de la Funcionalidad de Usuario',
        'descripcion': 'Implementar todas las funcionalidades relacionadas con la gestión de usuarios, incluyendo registro, inicio de sesión y recuperación de contraseña.',
        'criterios_aceptacion': 'Los usuarios deben poder registrarse, iniciar sesión y restablecer su contraseña sin errores.',
        'estado': 'En Progreso',
        'esfuerzo_estimado_total': 40,
        'fecha_inicio': '2024-01-01',
        'fecha_fin': '2024-01-31',
        'progreso': 0.2,
        'responsable_id': 1 
    },
    {
        'nombre': 'Mejoras en el Rendimiento del Sistema',
        'descripcion': 'Optimizar el rendimiento del sistema para reducir el tiempo de carga y mejorar la experiencia del usuario.',
        'criterios_aceptacion': 'El tiempo de carga debe ser menor a 2 segundos en condiciones normales.',
        'estado': 'Pendiente',
        'esfuerzo_estimado_total': 30,
        'fecha_inicio': '2024-02-01',
        'fecha_fin': '2024-02-15',
        'progreso': 0.1,
        'responsable_id': 2 
    },
    ]

    tareas = [
            {
        'titulo': 'Implementar Registro de Usuario',
        'descripcion': 'Desarrollar la funcionalidad que permite a los nuevos usuarios registrarse en la aplicación.',
        'criterios_aceptacion': 'El registro debe ser exitoso y enviar un correo de confirmación al usuario.',
        'prioridad': 'Alta',
        'estado': 'En Progreso',
        'esfuerzo_estimado': 10,
        'fecha_creacion': '2024-01-01',
        'fecha_actualizacion': '',
        'bloqueadores': '',
        'responsable_id': 1, 
        'sprint_asignado_id': 1 
    },
    {
        'titulo': 'Implementar Inicio de Sesión',
        'descripcion': 'Desarrollar la funcionalidad que permite a los usuarios existentes iniciar sesión.',
        'criterios_aceptacion': 'Los usuarios deben poder iniciar sesión con su correo y contraseña.',
        'prioridad': 'Alta',
        'estado': 'Pendiente',
        'esfuerzo_estimado': 8,
        'fecha_creacion': '',
        'fecha_actualizacion': '',
        'bloqueadores': '',
        'responsable_id': 2, 
        'sprint_asignado_id': 1
    },
    ]

    sprints = [
        {
        'nombre':'Sprint 1 - Funcionalidades Básicas',
        'objetivo':'Completar las funcionalidades básicas de usuario antes del final del mes.',
        'fecha_inicio':'2024-01-01',
        'fecha_fin':'2024-01-15',
        'velocidad':'20',
        'fecha_creacion':'2023-12-15', 
        'fecha_actualizacion':'2023-12-15', 
        'scrum_master_id':'1' 
    },
    {
        'nombre':'Sprint 2 - Mejoras de Rendimiento',
         'objetivo':'Optimizar el rendimiento del sistema basado en los resultados obtenidos del Sprint anterior.',
         'fecha_inicio':'2024-02-01',
         'fecha_fin':'2024-02-15',
         'velocidad':'25', 
         'fecha_creacion':'2024-01-15', 
         'fecha_actualizacion':'2024-01-15', 
         'scrum_master_id':'2' 
    },
    ]

   # autores = [
   #     {'nombre': 'Gabriel García Márquez', 'fecha_nacimiento': '1927-03-06'},
   #     {'nombre': 'J.K. Rowling', 'fecha_nacimiento': '1965-07-31'},
   #     # Agrega más autores según sea necesario
   # ] EJEMPLO!
    
    for epica_datos in epicas:
        epica = Epica.objects.create(
            nombre=epica_datos['nombre'],
            descripcion=epica_datos['descripcion'],
            criterios_aceptacion=epica_datos['criterios_aceptacion'],
            estado=epica_datos['estado'],
            esfuerzo_estimado_total=epica_datos['esfuerzo_estimado_total'],
            fecha_inicio=epica_datos['fecha_inicio'],
            fecha_fin=epica_datos['fecha_fin'],
            progreso=epica_datos['progreso'],
            responsable_id=epica_datos['responsable_id']
        )
    print(f'(Epica) {epica.nombre}: {epica.descripcion}. AGREGADO')

    for tarea_datos in tareas:
        tarea = Tarea(**tarea_datos)
        tarea.save()
        print(f'(Tarea) {tarea.titulo}: {tarea.descripcion}. AGREGADO')

    for sprint_datos in sprints:
        sprint = Sprint(**sprint_datos)
        sprint.save()
        print(f'(Sprint) {sprint.nombre}: {sprint.objetivo}. AGREGADO')

if __name__ == '__main__':
    populate()