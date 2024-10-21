from django.shortcuts import render
from .models import Epica, Sprint, Tarea, User
from django.http import JsonResponse

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