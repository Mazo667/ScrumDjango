# ACTIVIDAD GRUPA DE DJANGO SOBRE SCRUM

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