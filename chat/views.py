"""Main views for the chat app."""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages

from .models import Message, User


def user_select(req: HttpRequest) -> HttpResponse:
    """Provide a user selection page."""
    if req.method == "POST":
        user = req.POST.get("user")
        if user:
            username, created = User.objects.get_or_create(username=user)
            req.session["user"] = username.username
            if created:
                messages.success(req, f"New user {user}")
            return redirect("chat")
        else:
            messages.error(req, "Please select a user")
            return redirect("chat")
    else:
        return render(req, "chat/user_select.html")


def chat(req: HttpRequest) -> HttpResponse:
    """Show main chatroom."""
    user = req.session.get("user")
    if user:
        messages = Message.objects.all().order_by("created_at")
        return render(req, "chat/chat.html", {"user": user, "messages": messages})
    else:
        return redirect("user_select")


def send(req: HttpRequest) -> HttpResponse:
    """Create a new message."""
    if req.method != "POST":
        return HttpResponse(status=405)

    content = req.POST.get("content")
    user = req.session.get("user")
    if user and content:
        msg_user = User.objects.get(username=user)
        # Save the message
        Message.objects.create(user=msg_user, content=content)
        return redirect("chat")
    else:
        messages.error(req, "Message not provided!")
        return redirect("chat")
