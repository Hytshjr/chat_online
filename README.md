## Chat Onlinegit

ChatProject es una aplicación de chat en tiempo real construida con Django, Starlette, y Uvicorn.

## Características

- **Chat en Tiempo Real**: Permite a los usuarios enviar y recibir mensajes instantáneamente.
- **Soporte para WebSockets**: Utiliza WebSockets para mantener conexiones persistentes y de baja latencia.
- **Gestión de Conexiones**: Manejador de conexiones para gestionar múltiples salas de chat y usuarios.
- **Manejo de Errores**: Decorador de manejo de errores para capturar y registrar excepciones.

## Instalación

### Requisitos

- Python 3.8+
- Django 3.2+
- Starlette
- Uvicorn

### Instalación de Dependencias

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tuusuario/chatproject.git
    cd chatproject

2. Crea un entorno virtual y activa el entorno:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`

3. Instala las dependencias de producción:

    ```bash
    pip install -r requirements.txt

4. (Opcional) Instala las dependencias de desarrollo:

    ```bash
    pip install -r requirements-dev.txt
