"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from home.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()


from django.urls import path
ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi()),
    path('ws/new/', NewConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patterns)
})