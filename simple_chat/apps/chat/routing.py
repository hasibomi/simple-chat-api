from django.urls import path

from . import consumers


urlpatterns = [
    path('ws/chat/<room>', consumers.ChatConsumer.as_asgi()),
]
