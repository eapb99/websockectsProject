from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notify.consumer import *


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", EchoConsumer.as_asgi()),
        path("ws/", TickTockConsumer.as_asgi()),
        path("notifications/", NoseyConsumer.as_asgi()),
    ])
})