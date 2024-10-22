from django.urls import path
from . import views

urlpatterns = [
   path('sprints/', views.obtener_sprints, name='sprints_lista'),
   path('epicas/',views.obtener_epicas,name='epicas_lista'),
   path('tareas/',views.obtener_tareas,name='tareas_lista'),
   path('sprint/<int:sprint_id>/desarroladores/',views.obtener_equipo_de_desarrollo,name='desarrolladores_sprint'),
   path('sprint/<int:sprint_id>/backlog/',views.obtener_sprint_backlog,name='sprint_backlog')

]