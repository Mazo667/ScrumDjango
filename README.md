# ACTIVIDAD GRUPAL DE DJANGO SOBRE SCRUM

El objetivo de esta actividad es que los grupos conformados en la asignatura Programación
Web II apliquen los conceptos de modelado en Django teniendo en cuenta la metodología
SCRUM para gestionar proyectos (ver Anexo). Los grupos deben construir los modelos en
Django basados en las descripciones proporcionadas, generar un set de datos de prueba
utilizando las herramientas que prefieran, y proponer una mejora en los modelos.
Finalmente, deberán realizar consultas utilizando las relaciones y agregaciones vistas en
clase para demostrar el funcionamiento de los modelos.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Mazo667/ScrumDjango.git
   cd ScrumDjango
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala los paquetes requeridos:
    ```bash
    pip install -r requirements.txt
    ```

4. Poblamos la base de datos:
   ```bash
    python poblar_db.py
    ```

5. Ejecutamos el servidor
   ```bash
    python manage.py runserver
    ```

### URL DEFINIDOS

### Ejemplo de Uso

1. Para obtener una lista de todas las tareas:
    ```bash
    http://localhost:8000/scrum/tareas/
    ```

2. Para obtener los detalles de una tarea especifica con ID 1:
    ```bash
    http://localhost:8000/scrum/tareas/1
    ```

3. Para obtener las tareas creadas el 23 de octubre de 2024:
    ```bash
    http://localhost:8000/scrum/tareas/23-10-2024/
    ```

4. Para obtener una lista de todas las epicas:
    ```bash
    http://localhost:8000/scrum/epicas/
    ```

5. Para obtener los detalles de una epica especifica con ID 1:
    ```bash
    http://localhost:8000/scrum/epicas/1
    ```

6. Para obtener una lista de todas las sprints:
    ```bash
    http://localhost:8000/scrum/sprints/
    ```

7. Para obtener los detalles de una sprint especifica con ID 1:
    ```bash
    http://localhost:8000/scrum/sprints/1
    ```

8. Para obtener el equipo de desarrollo de una sprint especifica con ID 1:
    ```bash
    http://localhost:8000/scrum/sprints/1/desarrolladores
    ```

9. Para obtener una lista de la sprint backlog de una sprint especifica con ID 1:
    ```bash
    http://localhost:8000/scrum/sprints/1/backlog
    ```