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
        'progreso': 0.0,
        'responsable_id': 2 
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
        'progreso': 0.0,
        'responsable_id': 2 
    },
    {
        'id': 3,
        'nombre': 'Que la aplicacion web se pueda mostrar en cualquier dispositivo',
        'descripcion': 'Implementar funcionalidad en multiples dispositivos como PC de escritorios, Notebooks, Tablets y SmartPhones, para que puedan acceder a la aplicacion web.',
        'criterios_aceptacion': 'En SmartPhones deben mostrar menos animales para adoptar en la pantalla que en una PC de Escritorio.',
        'estado': 'POR_HACER',
        'esfuerzo_estimado_total': 30,
        'fecha_inicio': '2024-03-01',
        'fecha_fin': '2024-03-15',
        'progreso': 0.0,
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
        'scrum_master_id':'3' 
    },
    {
        'id': 2,
        'nombre':'Sprint 2 - Mejoras de Rendimiento',
        'objetivo':'Optimizar el rendimiento del sistema basado en los resultados obtenidos del Sprint anterior.',
        'fecha_inicio':'2024-02-01',
        'fecha_fin':'2024-02-15',
        'velocidad':'25', 
        'scrum_master_id':'3' 
    },
    {
        'id': 3,
        'nombre':'Sprint 3 - Pulir detalles',
        'objetivo':'Pulir detalles de la aplicacion web antes de la entrega.',
        'fecha_inicio':'2024-03-01',
        'fecha_fin':'2024-03-15',
        'velocidad':'22', 
        'scrum_master_id':'3' 
    },
    ]

    tareas = [
    {
        'id': 1,
        'titulo': 'Implementar Registro de Usuario',
        'descripcion': 'Desarrollar la funcionalidad que permite a los nuevos usuarios registrarse en la aplicación.',
        'criterios_aceptacion': 'El registro debe ser exitoso y enviar un correo de confirmación al usuario.',
        'prioridad': 'ALTA',
        'estado': 'COMPLETADA',
        'fecha_de_finalizacion' : '2024-05-01',
        'esfuerzo_estimado': 10,
        'bloqueadores': 'Falta definir cual servicio de envío de correos electrónicos se usara.',
        'responsable_id': 2, 
        'sprint_asignado_id': 1 
    },
    {
        'id': 2,
        'titulo': 'Implementar Inicio de Sesión',
        'descripcion': 'Desarrollar la funcionalidad que permite a los usuarios existentes iniciar sesión.',
        'criterios_aceptacion': 'Los usuarios deben poder iniciar sesión con su correo y contraseña.',
        'prioridad': 'ALTA',
        'estado': 'COMPLETADA',
        'fecha_de_finalizacion' : '2024-05-01',
        'esfuerzo_estimado': 8,
        'bloqueadores': '',
        'responsable_id': 2, 
        'sprint_asignado_id': 1
    },
    {
        'id': 3,
        'titulo': 'Desarrollar Formulario de Adopción',
        'descripcion': 'Crear un formulario para que los usuarios puedan solicitar la adopción de un animal.',
        'criterios_aceptacion': 'El formulario debe ser validado y enviar una notificación al administrador.',
        'prioridad': 'ALTA',
        'estado': 'COMPLETADA',
        'fecha_de_finalizacion' : '2024-05-01',
        'esfuerzo_estimado': 9,
        'bloqueadores': '',
        'responsable_id': 3,
        'sprint_asignado_id': 1
    },
    {
        'id': 4,
        'titulo': 'Implementar Gestión de Voluntarios',
        'descripcion': 'Desarrollar una sección para que los usuarios se registren como voluntarios.',
        'criterios_aceptacion': 'Los voluntarios deben poder completar un formulario y recibir confirmación.',
        'prioridad': 'ALTA',
        'estado': 'COMPLETADA',
        'fecha_de_finalizacion' : '2024-05-01',
        'esfuerzo_estimado': 10,
        'bloqueadores': '',
        'responsable_id': 4,
        'sprint_asignado_id': 1
    },
    {
        'id': 5,
        'titulo': 'Crear Apartado de Novedades',
        'descripcion': 'Desarrollar una sección donde se muestren las novedades sobre adopciones y eventos.',
        'criterios_aceptacion': 'Las novedades deben poder ser publicadas y vistas por los usuarios.',
        'prioridad': 'ALTA',
        'estado': 'COMPLETADA',
        'fecha_de_finalizacion' : '2024-05-01',
        'esfuerzo_estimado': 8,
        'bloqueadores': '',
        'responsable_id': 5,
        'sprint_asignado_id': 1 
    },
    {
        'id': 6,
        'titulo': 'Desarrollar Funcionalidad de Seguimiento',
        'descripcion': 'Implementar un sistema para que los administradores puedan hacer seguimiento a los adoptantes.',
        'criterios_aceptacion': 'Se debe poder registrar el estado de adopción y notas.',
        'prioridad': 'ALTA',
        'estado': 'COMPLETADA',
        'fecha_de_finalizacion' : '2024-05-01',
        'esfuerzo_estimado': 10,
        'bloqueadores': '',
        'responsable_id': 6,
        'sprint_asignado_id': 1 
    },
    {
        'id': 7,
        'titulo': 'Integrar Sistema de Notificaciones',
        'descripcion': 'Crear un sistema de notificaciones para informar a los usuarios sobre novedades y seguimientos.',
        'criterios_aceptacion': 'Los usuarios deben recibir notificaciones en su perfil.',
        'prioridad': 'ALTA',
        'estado': 'POR_HACER',
        "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 10,
        'bloqueadores': '',
        'responsable_id': 7,
        'sprint_asignado_id': 1
    },
    {
        'id': 8,
        'titulo': 'Implementar Reporte de Adopciones',
        'descripcion': 'Desarrollar un sistema para generar reportes de adopciones realizadas.',
        'criterios_aceptacion': 'Los administradores deben poder ver reportes detallados.',
        'prioridad': 'ALTA',
        'estado': 'POR_HACER',
        "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 6,
        'bloqueadores': '',
        'responsable_id': 8,
        'sprint_asignado_id': 1
    },
    {
        'id': 9,
        'titulo': 'Crear Página de FAQ',
        'descripcion': 'Desarrollar una sección de preguntas frecuentes para ayudar a los usuarios.',
        'criterios_aceptacion': 'Las preguntas deben ser fácilmente accesibles y navegables.',
        'prioridad': 'ALTA',
        'estado': 'POR_HACER',
        "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 5,
        'bloqueadores': '',
        'responsable_id': 9,
        'sprint_asignado_id': 1
    },
    {
        'id': 10,
        'titulo': 'Realizar Pruebas de Usabilidad',
        'descripcion': 'Ejecutar pruebas de usabilidad para asegurar que la aplicación es intuitiva para los usuarios.',
        'criterios_aceptacion': 'Se deben recopilar y analizar los comentarios de los usuarios.',
        'prioridad': 'ALTA',
        'estado': 'POR_HACER',
        "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 5,
        'bloqueadores': 'El uso de dispositivos moviles todavia no esta implementado el media query',
        'responsable_id': 10,
        'sprint_asignado_id': 1
    },
    {
        "id": 11,
        "titulo": "Optimizar Consultas SQL Lentas",
        "descripcion": "Identificar las consultas SQL más lentas del sistema y optimizarlas para mejorar el rendimiento general.",
        "criterios_aceptacion": "Las consultas optimizadas deben ejecutarse en menos de 1 segundo.",
        "prioridad": "ALTA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 8,
        "bloqueadores": "",
        "responsable_id": 3,
        "sprint_asignado_id": 2
    },
    {
        "id": 12,
        "titulo": "Implementar Mecanismo de Cacheo",
        "descripcion": "Desarrollar un sistema de cacheo para reducir el número de consultas a la base de datos en las páginas más visitadas.",
        "criterios_aceptacion": "Las páginas principales deben cargarse con tiempos de respuesta menores a 500 ms utilizando el sistema de cacheo.",
        "prioridad": "ALTA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 5,
        "bloqueadores": "Esperando aprobación para la selección de la herramienta de cacheo.",
        "responsable_id": 4,
        "sprint_asignado_id": 2
    },
    {
        "id": 13,
        "titulo": "Reducir Consumo de Memoria",
        "descripcion": "Revisar y optimizar el uso de memoria en las operaciones más intensivas del sistema para reducir el consumo general.",
        "criterios_aceptacion": "El consumo de memoria debe reducirse al menos en un 20% en las operaciones críticas.",
        "prioridad": "MEDIA",
        "estado": "EN_PROGRESO",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 10,
        "bloqueadores": "",
        "responsable_id": 5,
        "sprint_asignado_id": 2
    },
    {
        "id": 14,
        "titulo": "Optimizar Carga de Imágenes en la Web",
        "descripcion": "Implementar técnicas de lazy loading y compresión de imágenes para mejorar el tiempo de carga de las páginas que contienen multimedia.",
        "criterios_aceptacion": "Las imágenes deben cargarse de manera más rápida y las páginas deben mostrar mejoras en los tiempos de carga.",
        "prioridad": "MEDIA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 4,
        "bloqueadores": "Esperando aprobación de las herramientas de compresión.",
        "responsable_id": 2,
        "sprint_asignado_id": 2
    },
    {
        "id": 15,
        "titulo": "Optimizar Archivos Estáticos (CSS/JS)",
        "descripcion": "Minificar y combinar archivos CSS y JS para reducir el tiempo de carga y mejorar el rendimiento.",
        "criterios_aceptacion": "Los archivos estáticos deben reducir su tamaño en un 30% y mejorar los tiempos de carga de la página principal.",
        "prioridad": "ALTA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 3,
        "bloqueadores": "",
        "responsable_id": 1,
        "sprint_asignado_id": 2
    },
    {
        "id": 16,
        "titulo": "Configurar Herramientas de Monitoreo",
        "descripcion": "Implementar una herramienta de monitoreo en tiempo real para evaluar continuamente el rendimiento del sistema.",
        "criterios_aceptacion": "La herramienta de monitoreo debe estar configurada y mostrar informes sobre el uso de recursos del sistema en tiempo real.",
        "prioridad": "ALTA",
        "estado": "EN_PROGRESO",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 7,
        "bloqueadores": "Dependiente de la elección de la herramienta de monitoreo.",
        "responsable_id": 4,
        "sprint_asignado_id": 2
    },
    {
        "id": 17,
        "titulo": "Activar Compresión Gzip para Archivos Estáticos",
        "descripcion": "Configurar el servidor para utilizar compresión Gzip y reducir el tamaño de los archivos enviados al cliente.",
        "criterios_aceptacion": "Los archivos estáticos deben ser comprimidos y las transferencias deben ser más rápidas.",
        "prioridad": "MEDIA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 3,
        "bloqueadores": "",
        "responsable_id": 3,
        "sprint_asignado_id": 2
    },
    {
        "id": 18,
        "titulo": "Optimizar Llamadas a la API Externa",
        "descripcion": "Implementar técnicas de paginación y reducción de datos en las llamadas a la API externa para mejorar el tiempo de respuesta.",
        "criterios_aceptacion": "Las llamadas a la API deben tener un tiempo de respuesta inferior a 500 ms.",
        "prioridad": "MEDIA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 5,
        "bloqueadores": "Esperando validación de las opciones de la API.",
        "responsable_id": 2,
        "sprint_asignado_id": 2
    },
    {
        "id": 19,
        "titulo": "Mejorar la Escalabilidad Horizontal del Sistema",
        "descripcion": "Configurar el sistema para que pueda manejar una mayor cantidad de tráfico mediante la adición de nodos y la distribución de la carga.",
        "criterios_aceptacion": "El sistema debe poder escalar automáticamente en función de la carga de trabajo y soportar el doble de tráfico actual.",
        "prioridad": "ALTA",
        "estado": "EN_PROGRESO",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 10,
        "bloqueadores": "Dependiente de la configuración del balanceador de carga.",
        "responsable_id": 5,
        "sprint_asignado_id": 2
    },
    {
        "id": 20,
        "titulo": "Indexar Columnas Críticas en la Base de Datos",
        "descripcion": "Identificar columnas frecuentemente consultadas en la base de datos y crear índices para mejorar el rendimiento de las consultas.",
        "criterios_aceptacion": "Las consultas a la base de datos deben mejorar su tiempo de respuesta al menos en un 30%.",
        "prioridad": "ALTA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 6,
        "bloqueadores": "",
        "responsable_id": 4,
        "sprint_asignado_id": 2
    },
    {
        'id': 21,
        'titulo': 'Revisar diseño de la interfaz',
        'descripcion': 'Realizar una revisión final del diseño de la interfaz de usuario para asegurar que cumpla con los estándares.',
        'criterios_aceptacion': 'El diseño debe ser aprobado por el equipo de UI/UX.',
        'prioridad': 'ALTA',
        'estado': 'EN_PROGRESO',
        "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 5,
        'bloqueadores': '',
        'responsable_id': 2,
        'sprint_asignado_id': 3
    },
    {
        'id': 22,
        'titulo': 'Optimizar carga de imágenes',
        'descripcion': 'Reducir el tamaño de las imágenes para mejorar el tiempo de carga de la aplicación.',
        'criterios_aceptacion': 'Las imágenes deben cargarse en menos de 2 segundos.',
        'prioridad': "ALTA",
        'estado': "POR_HACER",
        "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 4,
        'bloqueadores': '',
        'responsable_id': 3,
        'sprint_asignado_id': 3
    },
    {
        'id': 23,
        'titulo': 'Corregir errores en el formulario de registro',
        'descripcion': 'Resolver los errores reportados en el formulario de registro.',
        'criterios_aceptacion': 'Todos los errores deben estar corregidos y documentados.',
        'prioridad': 'ALTA',
        'estado': "POR_HACER",
       "fecha_de_finalizacion" : None,
        'esfuerzo_estimado': 6,
        'bloqueadores': '',
        'responsable_id': 4,
        'sprint_asignado_id': 3
    },
    {
        'id': 24,
        'titulo': 'Actualizar documentación del proyecto',
        'descripcion': "Asegurarse de que toda la documentación del proyecto esté actualizada y sea accesible.",
        'criterios_aceptacion': "La documentación debe estar revisada y aprobada por el equipo.",
        'prioridad': "MEDIA",
        "estado": "POR_HACER",
        "fecha_de_finalizacion" : None,
        "esfuerzo_estimado": 3,
        "bloqueadores": "",
        "responsable_id": 5,
        "sprint_asignado_id": 3
    },
    {
       "id": 25,
       "titulo": "Implementar pruebas automatizadas",
       "descripcion": "Desarrollar pruebas automatizadas para las funcionalidades críticas.",
       "criterios_aceptacion": "Todas las pruebas deben pasar sin errores.",
       "prioridad": "ALTA",
       "estado": "POR_HACER",
       "fecha_de_finalizacion" : None,
       "esfuerzo_estimado": 7,
       "bloqueadores": "",
       "responsable_id": 6,
       "sprint_asignado_id": 3
   },
   {
       "id": 26,
       "titulo": "Realizar pruebas de usabilidad",
       "descripcion": "Ejecutar pruebas con usuarios para evaluar la usabilidad de la aplicación.",
       "criterios_aceptacion": "Los resultados deben ser documentados y presentados al equipo.",
       "prioridad": "MEDIA",
       "estado": "POR_HACER",
       "fecha_de_finalizacion" : None,
       "esfuerzo_estimado": 5,
       "bloqueadores": "",
       "responsable_id": 7,
       "sprint_asignado_id": 3
   },
   {
       "id": 27,
       "titulo": "Mejorar la velocidad de carga del sitio",
       "descripcion": "Optimizar el rendimiento del sitio web para mejorar los tiempos de carga.",
       "criterios_aceptacion": "'La velocidad de carga debe ser menor a 3 segundos en condiciones normales.",
       "prioridad": "ALTA",
       "estado" : "EN_PROGRESO",
       "fecha_de_finalizacion" : None,
       "esfuerzo_estimado" : 8,
       "bloqueadores" : "Necesita revisión del código existente.",
       "responsable_id" : 8,
       "sprint_asignado_id" : 3
   },
   {
      "id": 28,
      "titulo": "Revisar compatibilidad en navegadores",
      "descripcion": "Asegurarse de que la aplicación funcione correctamente en los principales navegadores.",
      "criterios_aceptacion": "La aplicación debe pasar pruebas en Chrome, Firefox y Safari.",
      "prioridad": "MEDIA",
      "estado": "POR_HACER",
      "fecha_de_finalizacion" : None,
      "esfuerzo_estimado": 4,
      "bloqueadores": "",
      "responsable_id": 9,
      "sprint_asignado_id": 3
   },
   {
      "id": 29,
      "titulo": "Implementar feedback del cliente",
      "descripcion": "Incorporar los comentarios recibidos del cliente sobre la última demo.",
      "criterios_aceptacion": "Los cambios deben ser revisados y aprobados por el cliente.",
      "prioridad": "ALTA",
      "estado": "POR_HACER",
      "fecha_de_finalizacion" : None,
      "esfuerzo_estimado": 6,
      "bloqueadores": "",
      "responsable_id": 10,
      "sprint_asignado_id": 3
   },
   {
      "id": 30,
      "titulo": "Preparar presentación para la entrega",
      "descripcion": "Crear una presentación que resuma las funcionalidades desarrolladas y los próximos pasos.",
      "criterios_aceptacion": "La presentación debe ser clara y estar lista antes de la reunión con el cliente.",
      "prioridad": "ALTA",
      "estado": "POR_HACER",
      "fecha_de_finalizacion" : None,
      "esfuerzo_estimado": 5,
      "bloqueadores": "",
      "responsable_id": 11,
      "sprint_asignado_id": 3
   }
     
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
            if usuario.id != 3:  #Excepto al scrum master o usuario con id 3
                sprint.equipo_de_desarrollo.add(usuario)

    for tarea_datos in tareas: #Foreach por cada tarea
        tarea = Tarea.objects.create(
            id=tarea_datos['id'],
            titulo=tarea_datos['titulo'],
            descripcion=tarea_datos['descripcion'],
            criterios_aceptacion=tarea_datos['criterios_aceptacion'],
            prioridad=tarea_datos['prioridad'],
            estado=tarea_datos['estado'],
            fecha_de_finalizacion=tarea_datos['fecha_de_finalizacion'],
            esfuerzo_estimado=tarea_datos['esfuerzo_estimado'],
            bloqueadores=tarea_datos['bloqueadores'],
            responsable_id=tarea_datos['responsable_id'],
            sprint_asignado_id=tarea_datos['sprint_asignado_id']
        )
        print(f'(Tarea) {tarea.titulo}: {tarea.descripcion} AGREGADO')
    
    #Obtengo los sprints para agregar las tareas manualmente
    sprint1 = Sprint.objects.get(id=1)
    tareas_objetos = Tarea.objects.filter(sprint_asignado=1)
    for tarea in tareas_objetos:
        sprint1.backlog_sprint.add(tarea)
        print(f'Tarea {tarea.titulo} agregada al Sprint {sprint1.nombre}')

    sprint2 = Sprint.objects.get(id=2)
    tareas_objetos = Tarea.objects.filter(sprint_asignado=2)
    for tarea in tareas_objetos:
        sprint2.backlog_sprint.add(tarea)
        print(f'Tarea {tarea.titulo} agregada al Sprint {sprint2.nombre}')

    sprint3 = Sprint.objects.get(id=3)
    tareas_objetos = Tarea.objects.filter(sprint_asignado=3)
    for tarea in tareas_objetos:
        sprint3.backlog_sprint.add(tarea)
        print(f'Tarea {tarea.titulo} agregada al Sprint {sprint3.nombre}')

    #Agrego las tareas asociadas a las epicas
    epica1 = Epica.objects.get(id=1)
    tareas_objetos = Tarea.objects.all()[:10]
    for tarea in tareas_objetos:
        epica1.tareas_asociadas.add(tarea)
        print(f'Tarea {tarea.titulo} asociada al Epica {epica1.nombre}')

    epica2 = Epica.objects.get(id=2)
    tareas_objetos = Tarea.objects.all()[10:20]
    for tarea in tareas_objetos:
        epica2.tareas_asociadas.add(tarea)
        print(f'Tarea {tarea.titulo} asociada al Epica {epica2.nombre}')

    epica3 = Epica.objects.get(id=2)
    tareas_objetos = Tarea.objects.all()[20:30]
    for tarea in tareas_objetos:
        epica3.tareas_asociadas.add(tarea)
        print(f'Tarea {tarea.titulo} asociada al Epica {epica3.nombre}')

    #Agrego las dependencias de las tareas
    tarea_por_asignar = Tarea.objects.get(id=2)
    tarea_para_asignar = Tarea.objects.get(id=1)
    tarea_por_asignar.dependencias.add(tarea_para_asignar) #Asigno la tarea 1 como una dependencia de la 2

    tarea_por_asignar = Tarea.objects.get(id=8)
    tarea_para_asignar = Tarea.objects.get(id=3)
    tarea_por_asignar.dependencias.add(tarea_para_asignar) #Asigno la tarea 3 como una dependencia de la 8
    
    tarea_por_asignar = Tarea.objects.get(id=10)
    tarea_para_asignar = Tarea.objects.get(id=11)
    tarea_por_asignar.dependencias.add(tarea_para_asignar) #Asigno la tarea 10 como una dependencia de la 11

    tarea_por_asignar = Tarea.objects.get(id=13)
    tarea_para_asignar = Tarea.objects.get(id=14)
    tarea_por_asignar.dependencias.add(tarea_para_asignar) #Asigno la tarea 13 como una dependencia de la 14

    tarea_por_asignar = Tarea.objects.get(id=20)
    tarea_para_asignar = Tarea.objects.get(id=11)
    tarea_por_asignar.dependencias.add(tarea_para_asignar) #Asigno la tarea 11 como una dependencia de la 20

    tarea_por_asignar = Tarea.objects.get(id=28)
    tarea_para_asignar = Tarea.objects.get(id=25)
    tarea_por_asignar.dependencias.add(tarea_para_asignar) #Asigno la tarea 25 como una dependencia de la 28

    #Agrego las dependencias de las epicas
    epica_por_asignar = Epica.objects.get(id=3)
    epica_para_asignar = Epica.objects.get(id=1)
    epica_por_asignar.dependencias.add(epica_para_asignar) #Asigno la epica 1 como una dependencia de la 3

if __name__ == '__main__':
    populate()