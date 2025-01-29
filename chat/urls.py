"""Urls for the chat application."""

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path(
        "user_select/", views.user_select, name="user_select"
    ),  # URL for user selection
    path("", views.chat, name="chat"),  # URL for chat interface
    path("send/", views.send, name="send"),  # URL for sending messages
]
