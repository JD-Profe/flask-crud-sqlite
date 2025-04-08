# flask-crud-sqlite

Aplicación web sencilla desarrollada con [Flask](https://flask.palletsprojects.com/) y [SQLite](https://www.sqlite.org/index.html) que permite gestionar una lista de tareas (To-Do List) con operaciones CRUD (crear, leer, actualizar y eliminar).

Diseñada con una interfaz responsiva usando [Bootstrap 5](https://getbootstrap.com/) y pensada para ejecutarse de forma local en un ordenador de escritorio o en móviles.

## Funcionalidades

- Añadir nuevas tareas con:
  - Descripción
  - Fecha de creación automática
  - Fecha límite (opcional)
  - Estado inicial: pendiente
- Ver la lista de tareas
- Marcar tareas como completadas
- Borrar tareas
- Interfaz adaptada a móviles

## Requisitos

- Python 3.8 o superior
- pip

## Instalación y ejecución

1. Clonar el repositorio:

```
git clone https://github.com/JD-Profe/flask-crud-sqlite.git
cd flask-crud-sqlite
```

2. Crear y activar un entorno virtual:

```
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

3. Instalar las dependencias:

```
pip install -r requirements.txt
```

4. (Opcional) Crear un archivo `.env` con la configuración de la base de datos:

```
echo DATABASE=tasks.db > .env
```

5. Ejecutar la aplicación:

```
python run.py
```

6. Abrir en el navegador:

```
http://127.0.0.1:5000
```

## Tecnologías utilizadas

- Python 3
- Flask
- SQLite
- Bootstrap 5
- HTML/CSS

## Licencia

Este proyecto se distribuye bajo la licencia MIT.

## Autor

Desarrollado por Jesús Domínguez como práctica de aprendizaje de Flask y desarrollo web.
