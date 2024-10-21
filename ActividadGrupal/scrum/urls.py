from django.urls import path
from . import views

urlpatterns = [
   path('sprints', views.obtener_sprints, name='sprints_lista'),
   path('epicas',views.obtener_epicas,name='epicas_lista'),
   path('tareas',views.obtener_tareas,name='tareas_lista')
]