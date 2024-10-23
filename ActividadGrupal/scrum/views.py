from django.shortcuts import render
from .models import Epica, Sprint, Tarea, User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

def obtener_epicas(request):
    epicas = Epica.objects.all().values()
    epicas_list = list(epicas)
    return JsonResponse(epicas_list,safe=False)

def obtener_epica_especifica(request,epica_id):
    tarea = get_object_or_404(Epica,id=epica_id)
    tareas_asociadas= list(tarea.tareas_asociadas.all().values())
    dependencias = list(tarea.dependencias.all().values())
    epica_dic = {
        'id':tarea.id,
        'nombre':tarea.nombre,
        'descripcion':tarea.descripcion,
        'criterios_aceptacion':tarea.criterios_aceptacion,
        'estado':tarea.estado,
        'responsable': {
            'id':tarea.responsable.id,
            'nombre':tarea.responsable.first_name,
            'apellido':tarea.responsable.last_name,
            'email':tarea.responsable.email,
            'usuario':tarea.responsable.username
        },
        'tareas_asociadas':tareas_asociadas,
        'esfuerzo_estimado_total':tarea.esfuerzo_estimado_total,
        'fecha_inicio':tarea.fecha_inicio,
        'fecha_fin':tarea.fecha_fin,
        'progreso':tarea.progreso,
        'dependencias': dependencias
    }
    return JsonResponse(epica_dic,safe=False)

def obtener_sprints(request):
    sprints = Sprint.objects.all().values()
    sprints_lista = list(sprints)
    return JsonResponse(sprints_lista,safe=False)

def obtener_equipo_de_desarrollo(request, sprint_id):
    sprint = get_object_or_404(Sprint, id=sprint_id)
    desarrolladores = sprint.equipo_de_desarrollo.all().values()  
    desarrolladores_list = list(desarrolladores) 
    return JsonResponse(desarrolladores_list, safe=False)

def obtener_sprint_backlog(request, sprint_id):
    sprint = get_object_or_404(Sprint, id=sprint_id)
    backlog = sprint.backlog_sprint.all().values()
    backlog_list = list(backlog) 
    return JsonResponse(backlog_list, safe=False)

def obtener_sprint_especifico(request,sprint_id):
    sprint = get_object_or_404(Sprint,id=sprint_id)
    desarrolladores_list = list(sprint.equipo_de_desarrollo.all().values())
    backlog_sprint = list(sprint.backlog_sprint.all().values())
    sprint_dic = {
        'id':sprint.id,
        'nombre':sprint.nombre,
        'objetivo':sprint.objetivo,
        'fecha_inicio':sprint.fecha_inicio,
        'fecha_fin':sprint.fecha_fin,
        'velocidad':sprint.velocidad,
        'scrum_master': {
            'id':sprint.scrum_master.id,
            'nombre':sprint.scrum_master.first_name,
            'apellido':sprint.scrum_master.last_name,
            'email':sprint.scrum_master.email,
            'usuario':sprint.scrum_master.username
        },
        'equipo_de_desarrollo': desarrolladores_list,
        'backlog_sprint': backlog_sprint,
        'fecha_creacion':sprint.fecha_creacion,
        'fecha_actualizacion':sprint.fecha_actualizacion,
    }
    return JsonResponse(sprint_dic,safe=False)

def obtener_tareas(request):
    tareas = Tarea.objects.all().values()
    tareas_list = list(tareas)
    return JsonResponse(tareas_list,safe=False)

def obtener_tarea_especifica(request,tarea_id):
    tarea = get_object_or_404(Tarea,id=tarea_id)
    sprint = tarea.sprint_asignado
    dependencias = list(tarea.dependencias.all().values())
    tarea_dic = {
        'titulo':tarea.titulo,
        'descripcion':tarea.descripcion,
        'criterios_aceptacion':tarea.criterios_aceptacion,
        'prioridad':tarea.prioridad,
        'estado':tarea.estado,
        'esfuerzo_estimado':tarea.esfuerzo_estimado,
        'responsable': {
            'id':tarea.responsable.id,
            'nombre':tarea.responsable.first_name,
            'apellido':tarea.responsable.last_name,
            'email':tarea.responsable.email,
            'usuario':tarea.responsable.username
        },
        'sprint_asignado': { 
            'id':sprint.id,
            'nombre':sprint.nombre,
            'objetivo':sprint.objetivo,
            'fecha_inicio':sprint.fecha_inicio,
            'fecha_fin':sprint.fecha_fin,
            'velocidad':sprint.velocidad,
            'scrum_master_id':sprint.scrum_master_id
              },
        'fecha_de_creacion':tarea.fecha_de_creacion,
        'fecha_de_actualizacion':tarea.fecha_de_actualizacion,
        'dependencias': dependencias,
        'bloqueadores':tarea.bloqueadores
    }
    return JsonResponse(tarea_dic)