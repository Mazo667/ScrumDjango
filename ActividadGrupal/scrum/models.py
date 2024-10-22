from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Sprint(models.Model):
    nombre = models.CharField(max_length=100)
    objetivo = models.TextField(
        blank=True,
        null=True
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    velocidad = models.IntegerField()
    scrum_master = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='sprint_como_scrum_master'
    )
    equipo_de_desarrollo = models.ManyToManyField(
        User,
        blank=True,
        related_name='sprint_como_desarrollador'
    )
    backlog_sprint = models.ManyToManyField(
        'Tarea',
        blank=True,
        related_name='sprint_backlog'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(velocidad__gte=0), name='velocidad_no_negativa'),
            models.CheckConstraint(
                check=Q(fecha_fin__gte=models.F('fecha_inicio')),
                name='fecha_fin_posterior'
            ),
        ]
    
    def __str__(self):
        return f"Sprint: {self.nombre} - Velocidad: {self.velocidad} - Fecha Inicio: {self.fecha_inicio} - Fecha Fin: {self.fecha_fin}"

ESTADOS = [
        ('POR_HACER', 'Por Hacer'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
    ]

class Epica(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    criterios_aceptacion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='POR_HACER')
    responsable = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True 
    )
    tareas_asociadas = models.ManyToManyField('Tarea', blank=True)
    esfuerzo_estimado_total = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    progreso = models.FloatField()
    dependencias = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(esfuerzo_estimado_total__gte=0),
                name='esfuerzo_total_no_negativo'
            ),
            models.CheckConstraint(
                check=Q(progreso__gte=0) & Q(progreso__lte=1),
                name='progreso_valido'
            ),
            models.CheckConstraint(check=Q(estado='POR_HACER') | Q(estado='EN_PROGRESO') | Q(estado='COMPLETADA'),
                name='estado_valido_epica'
            ),
            models.CheckConstraint(
                check=Q(fecha_fin__gte=models.F('fecha_inicio')),
                name='fecha_fin_posterior_epica'
            ),
        ]

class Tarea(models.Model):
    PRIORIDADES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(
        null=False,
        blank=True
    )
    criterios_aceptacion = models.TextField(
        blank=True,
        null=True
    )
    prioridad = models.CharField(
        max_length=10,
        choices=PRIORIDADES,
        default='BAJA' 
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='POR_HACER'
    )
    esfuerzo_estimado = models.IntegerField(
        null=True,
        blank=True  
    )
    responsable = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    sprint_asignado = models.ForeignKey(
        'Sprint',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    fecha_de_creacion = models.DateTimeField(auto_now=True)
    fecha_de_actualizacion = models.DateTimeField(auto_now_add=True)
    dependencias = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True
    )
    bloqueadores = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(estado='POR_HACER') | Q(estado='EN_PROGRESO') | Q(estado='COMPLETADA'), name='estado_valido_tarea'),
            models.CheckConstraint(check=Q(prioridad='BAJA') | Q(prioridad='MEDIA') | Q(prioridad='ALTA'), name='prioridad_valido_tarea'),
            models.CheckConstraint(check=Q(esfuerzo_estimado__gte=0), name='esfuerzo_estimado_no_negativo'),
        ]

    def __str__(self):
        return f"Tarea: {self.estado} - Prioridad: {self.prioridad} - Esfuerzo: {self.esfuerzo_estimado} - Responsable: {self.responsable}"
    
