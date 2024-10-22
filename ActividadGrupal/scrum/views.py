from django.shortcuts import render
from .models import Epica, Sprint, Tarea, User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

def obtener_sprints(request):
    sprints = Sprint.objects.all().values()
    sprints_lista = list(sprints)
    return JsonResponse(sprints_lista,safe=False)

def obtener_tareas(request):
    tareas = Tarea.objects.all().values()
    tareas_list = list(tareas)
    return JsonResponse(tareas_list,safe=False)

def obtener_epicas(request):
    epicas = Epica.objects.all().values()
    epicas_list = list(epicas)
    return JsonResponse(epicas_list,safe=False)

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