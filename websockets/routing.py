from django.urls import path

from . import consumers


ws_urlpatterns = [
    path('ws/redirect/', consumers.Consumer.as_asgi()),
]