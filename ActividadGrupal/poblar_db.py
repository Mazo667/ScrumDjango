import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ActividadGrupal.settings')
django.setup()

from django.core.management.base import BaseCommand #Comandos de django para usarlo como el shell
from scrum.models import Epica, Tarea, Sprint #Los modelos del scrum
from django.contrib.auth.models import User #Modelo del usuario


def populate():

    epicas = [
          {
        'id': 1,
        'nombre': 'Desarrollo de la Funcionalidad de Usuario',
        'descripcion': 'Implementar todas las funcionalidades relacionadas con la gestión de usuarios, incluyendo registro, inicio de sesión y recuperación de contraseña.',
        'criterios_aceptacion': 'Los usuarios deben poder registrarse, iniciar sesión y restablecer su contraseña sin errores.',
        'estado': 'EN_PROGRESO',
        'esfuerzo_estimado_total': 40,
        'fecha_inicio': '2024-01-01',
        'fecha_fin': '2024-01-31',
        'progreso': 0.2,
        'responsable_id': 1 
    },
    {
        'id': 2,
        'nombre': 'Mejoras en el Rendimiento del Sistema',
        'descripcion': 'Optimizar el rendimiento del sistema para reducir el tiempo de carga y mejorar la experiencia del usuario.',
        'criterios_aceptacion': 'El tiempo de carga debe ser menor a 2 segundos en condiciones normales.',
        'estado': 'POR_HACER',
        'esfuerzo_estimado_total': 30,
        'fecha_inicio': '2024-02-01',
        'fecha_fin': '2024-02-15',
        'progreso': 0.1,
        'responsable_id': 2 
    },
    ]

    sprints = [
        {
        'id': 1,
        'nombre':'Sprint 1 - Funcionalidades Básicas',
        'objetivo':'Completar las funcionalidades básicas de usuario antes del final del mes.',
        'fecha_inicio':'2024-01-01',
        'fecha_fin':'2024-01-15',
        'velocidad':'20',
        'scrum_master_id':'2' 
    },
    {
        'id': 2,
        'nombre':'Sprint 2 - Mejoras de Rendimiento',
         'objetivo':'Optimizar el rendimiento del sistema basado en los resultados obtenidos del Sprint anterior.',
         'fecha_inicio':'2024-02-01',
         'fecha_fin':'2024-02-15',
         'velocidad':'25', 
         'scrum_master_id':'2' 
    },
    {
        'id': 3,
        'nombre':'Sprint 3 - Pulir detalles',
         'objetivo':'Pulir detalles de la aplicacion web antes de la entrega.',
         'fecha_inicio':'2024-03-01',
         'fecha_fin':'2024-03-15',
         'velocidad':'22', 
         'scrum_master_id':'2' 
    },
    ]

    tareas = [
            {
        'id': 1,
        'titulo': 'Implementar Registro de Usuario',
        'descripcion': 'Desarrollar la funcionalidad que permite a los nuevos usuarios registrarse en la aplicación.',
        'criterios_aceptacion': 'El registro debe ser exitoso y enviar un correo de confirmación al usuario.',
        'prioridad': 'ALTA',
        'estado': 'EN_PROGRESO',
        'esfuerzo_estimado': 10,
        'bloqueadores': '',
        'responsable_id': 2, 
        'sprint_asignado_id': 1 
    },
    {
        'id': 2,
        'titulo': 'Implementar Inicio de Sesión',
        'descripcion': 'Desarrollar la funcionalidad que permite a los usuarios existentes iniciar sesión.',
        'criterios_aceptacion': 'Los usuarios deben poder iniciar sesión con su correo y contraseña.',
        'prioridad': 'ALTA',
        'estado': 'POR_HACER',
        'esfuerzo_estimado': 8,
        'bloqueadores': '',
        'responsable_id': 2, 
        'sprint_asignado_id': 1
    },
    {
        'id': 3,
        'titulo': 'Implementar Olvide mi contreña',
        'descripcion': 'Desarrollar la funcionalidad que permite a los usuarios restablecer su contraseña.',
        'criterios_aceptacion': 'Los usuarios deben poder restablecer su contraseña mediante su email.',
        'prioridad': 'MEDIA',
        'estado': 'POR_HACER',
        'esfuerzo_estimado': 7,
        'bloqueadores': '',
        'responsable_id': 2, 
        'sprint_asignado_id': 1
    },
    ]

    usuarios = User.objects.exclude(is_superuser=True) #Todos los usuarios excepto el admin

   # autores = [
   #     {'nombre': 'Gabriel García Márquez', 'fecha_nacimiento': '1927-03-06'},
   #     {'nombre': 'J.K. Rowling', 'fecha_nacimiento': '1965-07-31'},
   #     # Agrega más autores según sea necesario
   # ] EJEMPLO!
    
    for epica_datos in epicas: #Foreach por cada epica
        epica = Epica.objects.create(
            id=epica_datos['id'],
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
        print(f'(Epica) {epica.nombre}: {epica.descripcion} AGREGADO')

    for sprint_datos in sprints: #Foreach por cada sprint
        sprint = Sprint.objects.create(
            id=sprint_datos['id'],
            nombre=sprint_datos['nombre'],
            objetivo=sprint_datos['objetivo'],
            fecha_inicio=sprint_datos['fecha_inicio'],
            fecha_fin=sprint_datos['fecha_fin'],
            velocidad=sprint_datos['velocidad'],
            scrum_master_id=sprint_datos['scrum_master_id']
        )
        print(f'(Sprint) {sprint.nombre}: {sprint.objetivo} AGREGADO')
         #Agrego el equipo de desarrollo
        for usuario in usuarios:
            sprint.equipo_de_desarrollo.add(usuario)

    for tarea_datos in tareas: #Foreach por cada tarea
        tarea = Tarea.objects.create(
            id=tarea_datos['id'],
            titulo=tarea_datos['titulo'],
            descripcion=tarea_datos['descripcion'],
            criterios_aceptacion=tarea_datos['criterios_aceptacion'],
            prioridad=tarea_datos['prioridad'],
            estado=tarea_datos['estado'],
            esfuerzo_estimado=tarea_datos['esfuerzo_estimado'],
            bloqueadores=tarea_datos['bloqueadores'],
            responsable_id=tarea_datos['responsable_id'],
            sprint_asignado_id=tarea_datos['sprint_asignado_id']
        )
        print(f'(Tarea) {tarea.titulo}: {tarea.descripcion} AGREGADO')
    
    #Obtengo los sprints para agregar las tareas manualmente
    sprint1 = Sprint.objects.get(id=1)
    tareas_objetos = Tarea.objects.all().filter(sprint_asignado=1)
    for tarea in tareas_objetos:
        sprint1.backlog_sprint.add(tarea)
        print(f'Tarea {tarea.titulo} agregada al Sprint {sprint1.nombre}')

    sprint2 = Sprint.objects.get(id=2)
    tareas_objetos = Tarea.objects.all().filter(sprint_asignado=2)
    for tarea in tareas_objetos:
        sprint1.backlog_sprint.add(tarea)
        print(f'Tarea {tarea.titulo} agregada al Sprint {sprint1.nombre}')

    sprint3 = Sprint.objects.get(id=3)
    tareas_objetos = Tarea.objects.all().filter(sprint_asignado=3)
    for tarea in tareas_objetos:
        sprint1.backlog_sprint.add(tarea)
        print(f'Tarea {tarea.titulo} agregada al Sprint {sprint1.nombre}')

if __name__ == '__main__':
    populate()