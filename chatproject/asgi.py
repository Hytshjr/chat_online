"""
ASGI config for chatproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from chat_starlette.routing import websocket_routes
from starlette.applications import Starlette

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')
django.setup()

# Django ASGI application
django_asgi_app = get_asgi_application()

# Define Starlette app
starlette_app = Starlette(routes=websocket_routes)

# Combine Django and Starlette apps
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": starlette_app,
})
